#!/usr/bin/env python3

"""
Test sederhana untuk algoritma Ong-Schnorr-Shamir

File ini berisi unit test dasar untuk memverifikasi
implementasi algoritma bekerja dengan benar.
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
    """Test case untuk Digital Signature Scheme"""
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.ds = DigitalSignature()
    
    def test_sign_and_verify(self):
        """Test pembuatan dan verifikasi tanda tangan digital"""
        message = 12345
        
        # Test pembuatan tanda tangan
        s1, s2, r = self.ds.sign_message(message)
        
        self.assertIsInstance(s1, int)
        self.assertIsInstance(s2, int)
        self.assertIsInstance(r, int)
        
        # Test verifikasi tanda tangan
        is_valid = self.ds.verify_signature(message, s1, s2)
        self.assertTrue(is_valid)
    
    def test_invalid_signature(self):
        """Test verifikasi dengan tanda tangan yang salah"""
        message = 12345
        s1, s2, r = self.ds.sign_message(message)
        
        # Test dengan pesan yang berbeda
        invalid_message = message + 1
        is_valid = self.ds.verify_signature(invalid_message, s1, s2)
        self.assertFalse(is_valid)
        
        # Test dengan tanda tangan yang dimodifikasi
        modified_s1 = (s1 + 1) % self.ds.n
        is_valid = self.ds.verify_signature(message, modified_s1, s2)
        self.assertFalse(is_valid)
    
    def test_multiple_messages(self):
        """Test dengan beberapa pesan berbeda"""
        messages = [123, 456, 789, 999999, 1234567890]
        
        for message in messages:
            with self.subTest(message=message):
                s1, s2, r = self.ds.sign_message(message)
                is_valid = self.ds.verify_signature(message, s1, s2)
                self.assertTrue(is_valid)


class TestSubliminalChannel(unittest.TestCase):
    """Test case untuk Subliminal Channel Scheme"""
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.sc = SubliminalChannel()
    
    def test_subliminal_communication(self):
        """Test komunikasi saluran tersembunyi"""
        original_msg = 9876
        cover_msg = 5432
        
        # Test pembuatan pesan tersembunyi
        s1, s2, cover = self.sc.create_subliminal_message(original_msg, cover_msg)
        
        self.assertIsInstance(s1, int)
        self.assertIsInstance(s2, int)
        self.assertEqual(cover, cover_msg)
        
        # Test verifikasi pesan samaran (perspektif pihak ketiga)
        cover_valid = self.sc.verify_cover_message(cover, s1, s2)
        self.assertTrue(cover_valid)
        
        # Test dekripsi pesan asli (perspektif penerima sah)
        decrypted_msg = self.sc.decrypt_original_message(s1, s2)
        self.assertEqual(decrypted_msg, original_msg)
    
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
        
        for original, cover in scenarios:
            with self.subTest(original=original, cover=cover):
                try:
                    s1, s2, c = self.sc.create_subliminal_message(original, cover)
                    
                    # Test verifikasi pesan samaran
                    cover_valid = self.sc.verify_cover_message(c, s1, s2)
                    self.assertTrue(cover_valid)
                    
                    # Test dekripsi pesan asli
                    decrypted = self.sc.decrypt_original_message(s1, s2)
                    self.assertEqual(decrypted, original)
                    
                except ValueError:
                    # Skip jika pesan tidak relatif prima dengan n
                    continue


class TestSecurityProperties(unittest.TestCase):
    """Test case untuk properti keamanan"""
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.ds = DigitalSignature()
        self.sc = SubliminalChannel()
    
    def test_signature_uniqueness(self):
        """Test apakah tanda tangan berbeda untuk pesan berbeda"""
        message1 = 12345
        message2 = 54321
        
        s1_1, s2_1, r1 = self.ds.sign_message(message1)
        s1_2, s2_2, r2 = self.ds.sign_message(message2)
        
        # Tanda tangan harus berbeda untuk pesan berbeda
        self.assertNotEqual((s1_1, s2_1), (s1_2, s2_2))
    
    def test_random_signature_generation(self):
        """Test apakah tanda tangan menggunakan randomness"""
        message = 12345
        
        signatures = []
        for _ in range(5):
            s1, s2, r = self.ds.sign_message(message)
            signatures.append((s1, s2, r))
        
        # Setidaknya bilangan acak r harus berbeda
        r_values = [sig[2] for sig in signatures]
        unique_r = set(r_values)
        self.assertGreater(len(unique_r), 1, "Bilangan acak r harus bervariasi")
    
    def test_subliminal_channel_hiding(self):
        """Test apakah saluran tersembunyi benar-benar menyembunyikan pesan"""
        original_msg = 9876
        cover_msg1 = 1111
        cover_msg2 = 2222
        
        try:
            # Buat dua pesan tersembunyi dengan cover berbeda
            s1_1, s2_1, c1 = self.sc.create_subliminal_message(original_msg, cover_msg1)
            s1_2, s2_2, c2 = self.sc.create_subliminal_message(original_msg, cover_msg2)
            
            # Pesan samaran harus berbeda
            self.assertNotEqual(c1, c2)
            
            # Tanda tangan harus berbeda
            self.assertNotEqual((s1_1, s2_1), (s1_2, s2_2))
            
            # Tapi dekripsi harus menghasilkan pesan asli yang sama
            decrypted1 = self.sc.decrypt_original_message(s1_1, s2_1)
            decrypted2 = self.sc.decrypt_original_message(s1_2, s2_2)
            
            self.assertEqual(decrypted1, original_msg)
            self.assertEqual(decrypted2, original_msg)
            
        except ValueError:
            # Skip jika pesan tidak relatif prima dengan n
            self.skipTest("Pesan tidak relatif prima dengan n")


def run_tests():
    """Fungsi untuk menjalankan semua test"""
    print("=" * 60)
    print("MENJALANKAN UNIT TESTS ALGORITMA ONG-SCHNORR-SHAMIR")
    print("=" * 60)
    
    # Buat test suite
    suite = unittest.TestSuite()
    
    # Tambahkan test cases
    test_classes = [
        TestOngSchnorrShamir,
        TestDigitalSignature,
        TestSubliminalChannel,
        TestSecurityProperties
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Jalankan tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print hasil
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("✅ SEMUA TESTS BERHASIL!")
        print(f"Total tests: {result.testsRun}")
    else:
        print("❌ ADA TESTS YANG GAGAL!")
        print(f"Total tests: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
