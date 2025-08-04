#!/usr/bin/env python3

"""
Test untuk algoritma Ong-Schnorr-Shamir yang SUDAH DIPERBAIKI

MAJOR UPDATE: Test ini sekarang menguji implementasi yang benar,
bukan lagi memberikan "rasa aman palsu" seperti sebelumnya.
FIXED: SyntaxError dengan backslash dalam f-string sudah diperbaiki.

File ini berisi unit test untuk memverifikasi bahwa implementasi
algoritma yang sudah diperbaiki bekerja dengan benar.
"""

import sys
import os
import unittest
import random
import math

# Tambahkan path untuk import module
sys.path.insert(0, os.path.dirname(__file__))

from ong_schnorr_shamir import (
    OngSchnorrShamir, 
    DigitalSignature, 
    SubliminalChannel, 
    generate_keys
)


class TestOngSchnorrShamir(unittest.TestCase):
    """Test case untuk class OngSchnorrShamir dasar"""
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.oss = OngSchnorrShamir()
    
    def test_initialization(self):
        """Test inisialisasi objek"""
        self.assertIsInstance(self.oss.n, int)
        self.assertIsInstance(self.oss.k, int)
        self.assertIsInstance(self.oss.h, int)
        
        # Test apakah n dan k relatif prima
        self.assertEqual(math.gcd(self.oss.n, self.oss.k), 1)
    
    def test_key_generation(self):
        """Test pembuatan kunci"""
        n, k, h = generate_keys(256)
        
        self.assertIsInstance(n, int)
        self.assertIsInstance(k, int)
        self.assertIsInstance(h, int)
        
        # Test apakah kunci valid
        self.assertEqual(math.gcd(n, k), 1)
        self.assertGreater(n, 0)
        self.assertGreater(k, 0)


class TestDigitalSignature(unittest.TestCase):
    """
    Test case untuk Digital Signature Scheme
    
    FIXED VERSION: Test ini sekarang menguji implementasi yang benar
    """
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.ds = DigitalSignature()
    
    def test_sign_and_verify_basic(self):
        """Test dasar pembuatan dan verifikasi tanda tangan digital"""
        message = 12345
        
        # Test pembuatan tanda tangan
        s1, s2, r = self.ds.sign_message(message)
        
        self.assertIsInstance(s1, int)
        self.assertIsInstance(s2, int)
        self.assertIsInstance(r, int)
        
        # Test verifikasi tanda tangan - INI YANG PALING PENTING!
        is_valid = self.ds.verify_signature(message, s1, s2)
        self.assertTrue(is_valid, "Signature verification should pass with correct implementation!")
    
    def test_signature_security(self):
        """Test keamanan tanda tangan - harus GAGAL untuk modifikasi"""
        message = 12345
        s1, s2, r = self.ds.sign_message(message)
        
        # Test dengan pesan yang berbeda - HARUS GAGAL
        invalid_message = message + 1
        is_valid = self.ds.verify_signature(invalid_message, s1, s2)
        self.assertFalse(is_valid, "Modified message should fail verification!")
        
        # Test dengan tanda tangan yang dimodifikasi - HARUS GAGAL
        modified_s1 = (s1 + 1) % self.ds.n
        is_valid = self.ds.verify_signature(message, modified_s1, s2)
        self.assertFalse(is_valid, "Modified S1 should fail verification!")
        
        modified_s2 = (s2 + 1) % self.ds.n
        is_valid = self.ds.verify_signature(message, s1, modified_s2)
        self.assertFalse(is_valid, "Modified S2 should fail verification!")
    
    def test_multiple_messages(self):
        """Test dengan beberapa pesan berbeda"""
        messages = [123, 456, 789, 999999, 1234567890]
        
        for message in messages:
            with self.subTest(message=message):
                s1, s2, r = self.ds.sign_message(message)
                is_valid = self.ds.verify_signature(message, s1, s2)
                self.assertTrue(is_valid, f"Signature verification failed for message {message}")
    
    def test_signature_randomness(self):
        """Test apakah tanda tangan menggunakan randomness yang benar"""
        message = 12345
        
        signatures = []
        for _ in range(5):
            s1, s2, r = self.ds.sign_message(message)
            signatures.append((s1, s2, r))
            
            # Setiap signature harus valid
            is_valid = self.ds.verify_signature(message, s1, s2)
            self.assertTrue(is_valid, "Each signature should be valid")
        
        # Bilangan acak r harus bervariasi
        r_values = [sig[2] for sig in signatures]
        unique_r = set(r_values)
        self.assertGreater(len(unique_r), 1, "Random values r should vary")


class TestSubliminalChannel(unittest.TestCase):
    """
    Test case untuk Subliminal Channel Scheme
    
    FIXED VERSION: Test ini sekarang menguji implementasi yang benar
    """
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.sc = SubliminalChannel()
    
    def test_subliminal_communication_basic(self):
        """Test dasar komunikasi saluran tersembunyi"""
        original_msg = 9876
        cover_msg = 5432
        
        try:
            # Test pembuatan pesan tersembunyi
            s1, s2, cover = self.sc.create_subliminal_message(original_msg, cover_msg)
            
            self.assertIsInstance(s1, int)
            self.assertIsInstance(s2, int)
            self.assertEqual(cover, cover_msg)
            
            # Test verifikasi pesan samaran (perspektif pihak ketiga)
            cover_valid = self.sc.verify_cover_message(cover, s1, s2)
            self.assertTrue(cover_valid, "Cover message verification should pass!")
            
            # Test dekripsi pesan asli (perspektif penerima sah) - INI YANG PALING PENTING!
            decrypted_msg = self.sc.decrypt_original_message(s1, s2)
            self.assertEqual(decrypted_msg, original_msg, "Decryption should recover original message!")
            
        except ValueError:
            # Skip jika pesan tidak relatif prima dengan n
            self.skipTest("Messages not coprime with n")
    
    def test_subliminal_security(self):
        """Test keamanan saluran tersembunyi"""
        original_msg = 111
        cover_msg = 222
        
        try:
            s1, s2, cover = self.sc.create_subliminal_message(original_msg, cover_msg)
            
            # Pihak ketiga hanya bisa verifikasi pesan samaran
            cover_valid = self.sc.verify_cover_message(cover, s1, s2)
            self.assertTrue(cover_valid, "Third party should see valid cover message")
            
            # Penerima sah bisa mendapatkan pesan asli
            decrypted = self.sc.decrypt_original_message(s1, s2)
            self.assertEqual(decrypted, original_msg, "Legitimate receiver should get original message")
            
            # Test dengan cover message yang salah - HARUS GAGAL
            wrong_cover = cover + 1
            cover_invalid = self.sc.verify_cover_message(wrong_cover, s1, s2)
            self.assertFalse(cover_invalid, "Wrong cover message should fail verification")
            
        except ValueError:
            self.skipTest("Messages not coprime with n")
    
    def test_invalid_messages(self):
        """Test dengan pesan yang tidak valid"""
        # Test dengan pesan yang tidak relatif prima dengan n
        invalid_msg = self.sc.n  # Pasti tidak relatif prima
        valid_msg = 123
        
        with self.assertRaises(ValueError):
            self.sc.create_subliminal_message(invalid_msg, valid_msg)
        
        with self.assertRaises(ValueError):
            self.sc.create_subliminal_message(valid_msg, invalid_msg)
    
    def test_multiple_scenarios(self):
        """Test dengan beberapa skenario berbeda"""
        scenarios = [
            (111, 222),
            (777, 888),
            (123456, 654321),
            (999, 111)
        ]
        
        success_count = 0
        for original, cover in scenarios:
            with self.subTest(original=original, cover=cover):
                try:
                    s1, s2, c = self.sc.create_subliminal_message(original, cover)
                    
                    # Test verifikasi pesan samaran
                    cover_valid = self.sc.verify_cover_message(c, s1, s2)
                    self.assertTrue(cover_valid, f"Cover verification failed for {original}/{cover}")
                    
                    # Test dekripsi pesan asli
                    decrypted = self.sc.decrypt_original_message(s1, s2)
                    self.assertEqual(decrypted, original, f"Decryption failed for {original}/{cover}")
                    
                    success_count += 1
                    
                except ValueError:
                    # Skip jika pesan tidak relatif prima dengan n
                    continue
        
        # Setidaknya beberapa skenario harus berhasil
        self.assertGreater(success_count, 0, "At least some scenarios should work")


class TestMathematicalProperties(unittest.TestCase):
    """
    Test case untuk properti matematis algoritma
    
    NEW: Test yang memverifikasi aljabar di balik algoritma
    """
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.ds = DigitalSignature()
        self.sc = SubliminalChannel()
    
    def test_signature_mathematical_correctness(self):
        """Test apakah formula matematis signature benar"""
        message = 12345
        s1, s2, r = self.ds.sign_message(message)
        
        # Verifikasi manual menggunakan formula: S1^2 + h * S2^2 ≡ M (mod n)
        left_side = (pow(s1, 2, self.ds.n) + (self.ds.h * pow(s2, 2, self.ds.n))) % self.ds.n
        right_side = message % self.ds.n
        
        self.assertEqual(left_side, right_side, "Mathematical formula S1^2 + h*S2^2 ≡ M should hold")
    
    def test_subliminal_mathematical_correctness(self):
        """Test apakah formula matematis subliminal channel benar"""
        original_msg = 777
        cover_msg = 888
        
        try:
            s1, s2, cover = self.sc.create_subliminal_message(original_msg, cover_msg)
            
            # Test formula verifikasi: S1^2 + h * S2^2 ≡ w' (mod n)
            left_side = (pow(s1, 2, self.sc.n) + (self.sc.h * pow(s2, 2, self.sc.n))) % self.sc.n
            right_side = cover % self.sc.n
            
            self.assertEqual(left_side, right_side, "Mathematical formula S1^2 + h*S2^2 ≡ w' should hold")
            
            # Test formula dekripsi: w = S1 - k^-1 * S2
            k_inv = pow(self.sc.k, -1, self.sc.n)
            calculated_w = (s1 - (k_inv * s2)) % self.sc.n
            
            self.assertEqual(calculated_w, original_msg, "Mathematical formula w = S1 - k^-1*S2 should hold")
            
        except ValueError:
            self.skipTest("Messages not coprime with n")
    
    def test_key_properties(self):
        """Test properti kunci yang dihasilkan"""
        # Test GCD
        self.assertEqual(math.gcd(self.ds.n, self.ds.k), 1, "n and k should be coprime")
        
        # Test nilai h
        k_inv = pow(self.ds.k, -1, self.ds.n)
        expected_h = (-(k_inv ** 2)) % self.ds.n
        self.assertEqual(self.ds.h, expected_h, "h should be calculated correctly")


def run_tests():
    """Fungsi untuk menjalankan semua test yang sudah diperbaiki"""
    print("=" * 70)
    print("🔧 MENJALANKAN UNIT TESTS UNTUK ALGORITMA YANG SUDAH DIPERBAIKI")
    print("=" * 70)
    print("MAJOR UPDATE: Test ini sekarang menguji implementasi yang benar!")
    print("- Bug formula S2 sudah diperbaiki")
    print("- Bug formula dekripsi subliminal sudah diperbaiki")
    print("- Test tidak lagi memberikan 'rasa aman palsu'")
    print("- FIXED: SyntaxError dengan backslash dalam f-string")
    print("=" * 70)
    
    # Buat test suite
    suite = unittest.TestSuite()
    
    # Tambahkan test cases
    test_classes = [
        TestOngSchnorrShamir,
        TestDigitalSignature,
        TestSubliminalChannel,
        TestMathematicalProperties
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Jalankan tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print hasil
    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉 SEMUA TESTS BERHASIL!")
        print("✅ Algoritma sekarang bekerja dengan benar!")
        print(f"📊 Total tests: {result.testsRun}")
        print("🔧 Bug matematis fundamental sudah diperbaiki!")
    else:
        print("❌ ADA TESTS YANG GAGAL!")
        print(f"📊 Total tests: {result.testsRun}")
        print(f"❌ Failures: {len(result.failures)}")
        print(f"❌ Errors: {len(result.errors)}")
        
        # FIXED: Handle backslash in f-string properly
        if result.failures:
            print("\n🔍 FAILURES:")
            for test, traceback_text in result.failures:
                # Split outside of f-string to avoid backslash issues
                error_parts = traceback_text.split('AssertionError: ')
                if len(error_parts) > 1:
                    error_message = error_parts[-1].splitlines()[0]
                else:
                    error_message = "Unknown error"
                print(f"- {test}: {error_message}")
        
        if result.errors:
            print("\n🔍 ERRORS:")
            for test, traceback_text in result.errors:
                # Split outside of f-string to avoid backslash issues
                error_lines = traceback_text.splitlines()
                error_message = error_lines[-1] if error_lines else "Unknown error"
                print(f"- {test}: {error_message}")
    
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    
    if success:
        print("\n🚀 READY TO GO!")
        print("Algoritma sudah diperbaiki dan siap digunakan!")
        print("🔧 FIXED: Test runner tidak akan crash lagi!")
    else:
        print("\n⚠️  NEEDS MORE WORK")
        print("Masih ada masalah yang perlu diperbaiki.")
    
    sys.exit(0 if success else 1)
