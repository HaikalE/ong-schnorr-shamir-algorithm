#!/usr/bin/env python3

"""
Contoh penggunaan algoritma Ong-Schnorr-Shamir

File ini berisi berbagai contoh implementasi dan penggunaan
algoritma Ong-Schnorr-Shamir untuk Digital Signature dan Subliminal Channel.
"""

from ong_schnorr_shamir import DigitalSignature, SubliminalChannel, generate_keys
import time


def example_digital_signature():
    """
    Contoh penggunaan skema tanda tangan digital
    """
    print("="*60)
    print("CONTOH DIGITAL SIGNATURE SCHEME")
    print("="*60)
    
    # Inisialisasi dengan kunci yang sudah ditentukan
    print("\n1. Inisialisasi sistem...")
    ds = DigitalSignature()
    
    print(f"   Kunci publik (n): {ds.n}")
    print(f"   Kunci privat (k): {ds.k}")
    print(f"   Nilai h: {ds.h}")
    
    # Pesan yang akan ditandatangani
    messages = [12345, 98765, 555666, 123456789]
    
    print("\n2. Proses tanda tangan digital:")
    for i, message in enumerate(messages, 1):
        print(f"\n   Pesan {i}: {message}")
        
        # Buat tanda tangan
        start_time = time.time()
        s1, s2, r = ds.sign_message(message)
        sign_time = time.time() - start_time
        
        print(f"   Tanda tangan S1: {s1}")
        print(f"   Tanda tangan S2: {s2}")
        print(f"   Bilangan acak r: {r}")
        print(f"   Waktu pembuatan tanda tangan: {sign_time:.6f} detik")
        
        # Verifikasi tanda tangan
        start_time = time.time()
        is_valid = ds.verify_signature(message, s1, s2)
        verify_time = time.time() - start_time
        
        print(f"   Hasil verifikasi: {'✓ VALID' if is_valid else '✗ INVALID'}")
        print(f"   Waktu verifikasi: {verify_time:.6f} detik")
        
        # Test dengan pesan yang dimodifikasi
        modified_message = message + 1
        is_valid_modified = ds.verify_signature(modified_message, s1, s2)
        print(f"   Verifikasi pesan yang dimodifikasi ({modified_message}): {'✓ VALID' if is_valid_modified else '✗ INVALID (Expected)'}")


def example_subliminal_channel():
    """
    Contoh penggunaan skema saluran tersembunyi
    """
    print("\n\n" + "="*60)
    print("CONTOH SUBLIMINAL CHANNEL SCHEME")
    print("="*60)
    
    # Inisialisasi sistem
    print("\n1. Inisialisasi sistem...")
    sc = SubliminalChannel()
    
    print(f"   Kunci publik (n): {sc.n}")
    print(f"   Kunci privat (k): {sc.k}")
    print(f"   Nilai h: {sc.h}")
    
    # Skenario komunikasi tersembunyi
    scenarios = [
        {"original": 111111, "cover": 222222, "description": "Komunikasi rahasia 1"},
        {"original": 987654, "cover": 123456, "description": "Komunikasi rahasia 2"},
        {"original": 555555, "cover": 999999, "description": "Komunikasi rahasia 3"}
    ]
    
    print("\n2. Proses komunikasi saluran tersembunyi:")
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n   --- {scenario['description']} ---")
        original_msg = scenario['original']
        cover_msg = scenario['cover']
        
        print(f"   Pesan asli (rahasia): {original_msg}")
        print(f"   Pesan samaran (publik): {cover_msg}")
        
        try:
            # Buat pesan tersembunyi
            start_time = time.time()
            s1, s2, cover = sc.create_subliminal_message(original_msg, cover_msg)
            create_time = time.time() - start_time
            
            print(f"   Tanda tangan S1: {s1}")
            print(f"   Tanda tangan S2: {s2}")
            print(f"   Waktu pembuatan: {create_time:.6f} detik")
            
            # Simulasi verifikasi oleh pihak ketiga (hanya melihat pesan samaran)
            print("\n   [Perspektif Pihak Ketiga]")
            start_time = time.time()
            cover_valid = sc.verify_cover_message(cover, s1, s2)
            verify_time = time.time() - start_time
            
            print(f"   Pesan yang terlihat: {cover}")
            print(f"   Verifikasi pesan samaran: {'✓ VALID' if cover_valid else '✗ INVALID'}")
            print(f"   Waktu verifikasi: {verify_time:.6f} detik")
            print(f"   Status: Pihak ketiga hanya melihat pesan samaran")
            
            # Simulasi dekripsi oleh penerima sah
            print("\n   [Perspektif Penerima Sah]")
            start_time = time.time()
            decrypted_msg = sc.decrypt_original_message(s1, s2)
            decrypt_time = time.time() - start_time
            
            print(f"   Pesan yang didekripsi: {decrypted_msg}")
            print(f"   Dekripsi berhasil: {'✓ Ya' if decrypted_msg == original_msg else '✗ Tidak'}")
            print(f"   Waktu dekripsi: {decrypt_time:.6f} detik")
            
        except Exception as e:
            print(f"   ✗ Error: {e}")


def example_key_generation():
    """
    Contoh pembuatan kunci dengan berbagai ukuran
    """
    print("\n\n" + "="*60)
    print("CONTOH PEMBUATAN KUNCI")
    print("="*60)
    
    key_sizes = [256, 512, 1024]
    
    for size in key_sizes:
        print(f"\nMembuat kunci {size}-bit...")
        start_time = time.time()
        
        try:
            n, k, h = generate_keys(size)
            generation_time = time.time() - start_time
            
            print(f"   Kunci publik (n): {n}")
            print(f"   Kunci privat (k): {k}")
            print(f"   Nilai h: {h}")
            print(f"   Panjang n dalam bit: {n.bit_length()}")
            print(f"   Waktu pembuatan: {generation_time:.6f} detik")
            
            # Verifikasi apakah kunci valid
            import math
            gcd_check = math.gcd(n, k)
            print(f"   GCD(n,k) = {gcd_check} {'✓' if gcd_check == 1 else '✗'}")
            
        except Exception as e:
            print(f"   ✗ Error dalam pembuatan kunci: {e}")


def example_security_test():
    """
    Contoh test keamanan sederhana
    """
    print("\n\n" + "="*60)
    print("TEST KEAMANAN SEDERHANA")
    print("="*60)
    
    ds = DigitalSignature()
    
    print("\n1. Test modifikasi tanda tangan:")
    message = 123456
    s1, s2, r = ds.sign_message(message)
    
    print(f"   Pesan asli: {message}")
    print(f"   Tanda tangan asli (S1, S2): ({s1}, {s2})")
    
    # Test dengan tanda tangan yang dimodifikasi
    modified_signatures = [
        (s1 + 1, s2, "S1 + 1"),
        (s1, s2 + 1, "S2 + 1"),
        (s1 + 1, s2 + 1, "S1 + 1, S2 + 1")
    ]
    
    for mod_s1, mod_s2, description in modified_signatures:
        is_valid = ds.verify_signature(message, mod_s1, mod_s2)
        print(f"   Verifikasi dengan {description}: {'✗ INVALID (Expected)' if not is_valid else '✓ VALID (Unexpected!)'}")
    
    print("\n2. Test dengan pesan berbeda:")
    different_messages = [message + i for i in range(1, 6)]
    
    for msg in different_messages:
        is_valid = ds.verify_signature(msg, s1, s2)
        print(f"   Verifikasi pesan {msg}: {'✗ INVALID (Expected)' if not is_valid else '✓ VALID (Unexpected!)'}")


def main():
    """
    Fungsi utama untuk menjalankan semua contoh
    """
    print("ALGORITMA ONG-SCHNORR-SHAMIR")
    print("Implementasi Digital Signature dan Subliminal Channel")
    print("\nDibuat oleh: [Nama Anda]")
    print("Tanggal:", time.strftime("%Y-%m-%d %H:%M:%S"))
    
    try:
        # Jalankan semua contoh
        example_digital_signature()
        example_subliminal_channel()
        example_key_generation()
        example_security_test()
        
        print("\n\n" + "="*60)
        print("SEMUA CONTOH SELESAI DIJALANKAN")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\n\nTerjadi error: {e}")


if __name__ == "__main__":
    main()
