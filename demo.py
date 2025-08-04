#!/usr/bin/env python3

"""
Demo Interaktif Algoritma Ong-Schnorr-Shamir

Script ini menyediakan interface interaktif untuk mencoba
algoritma Ong-Schnorr-Shamir secara langsung.
"""

import sys
import time
import random
from ong_schnorr_shamir import DigitalSignature, SubliminalChannel, generate_keys


def print_header():
    """Print header yang menarik"""
    print("\n" + "="*70)
    print("🔐 DEMO INTERAKTIF ALGORITMA ONG-SCHNORR-SHAMIR 🔐")
    print("="*70)
    print("Algoritma kriptografi untuk Digital Signature dan Subliminal Channel")
    print("Dibuat oleh: HaikalE | GitHub: @HaikalE")
    print("="*70 + "\n")


def print_menu():
    """Print menu utama"""
    print("\n📋 MENU UTAMA:")
    print("1. 📝 Demo Digital Signature Scheme")
    print("2. 🔍 Demo Subliminal Channel Scheme")
    print("3. 🔑 Generate Kunci Baru")
    print("4. 🧪 Test Keamanan")
    print("5. 📊 Benchmark Performa")
    print("6. ❓ Bantuan & Penjelasan")
    print("0. 🚪 Keluar")
    print("-" * 50)


def demo_digital_signature():
    """Demo interaktif untuk digital signature"""
    print("\n🔐 DEMO DIGITAL SIGNATURE SCHEME")
    print("="*50)
    
    print("\n⚙️  Inisialisasi sistem...")
    ds = DigitalSignature()
    
    print(f"✅ Kunci publik (n): {ds.n}")
    print(f"✅ Kunci privat (k): {ds.k}")
    print(f"✅ Nilai h: {ds.h}")
    
    while True:
        print("\n📝 Pilihan:")
        print("1. Masukkan pesan sendiri")
        print("2. Gunakan pesan contoh")
        print("3. Kembali ke menu utama")
        
        choice = input("\nPilih opsi (1-3): ").strip()
        
        if choice == "1":
            try:
                message = int(input("Masukkan pesan (angka): "))
            except ValueError:
                print("❌ Pesan harus berupa angka!")
                continue
                
        elif choice == "2":
            message = random.randint(10000, 999999)
            print(f"📋 Menggunakan pesan contoh: {message}")
            
        elif choice == "3":
            return
            
        else:
            print("❌ Pilihan tidak valid!")
            continue
        
        print(f"\n🔄 Memproses pesan: {message}")
        
        # Buat tanda tangan
        start_time = time.time()
        s1, s2, r = ds.sign_message(message)
        sign_time = time.time() - start_time
        
        print(f"✅ Tanda tangan S1: {s1}")
        print(f"✅ Tanda tangan S2: {s2}")
        print(f"✅ Bilangan acak r: {r}")
        print(f"⏱️  Waktu pembuatan: {sign_time:.6f} detik")
        
        # Verifikasi
        start_time = time.time()
        is_valid = ds.verify_signature(message, s1, s2)
        verify_time = time.time() - start_time
        
        print(f"\n🔍 Hasil verifikasi: {'✅ VALID' if is_valid else '❌ INVALID'}")
        print(f"⏱️  Waktu verifikasi: {verify_time:.6f} detik")
        
        # Test dengan pesan yang dimodifikasi
        modified_message = message + 1
        is_valid_modified = ds.verify_signature(modified_message, s1, s2)
        print(f"🔍 Verifikasi pesan dimodifikasi ({modified_message}): {'✅ VALID' if is_valid_modified else '❌ INVALID (Expected)'}")
        
        input("\n📱 Tekan Enter untuk melanjutkan...")


def demo_subliminal_channel():
    """Demo interaktif untuk subliminal channel"""
    print("\n🕵️  DEMO SUBLIMINAL CHANNEL SCHEME")
    print("="*50)
    
    print("\n⚙️  Inisialisasi sistem...")
    sc = SubliminalChannel()
    
    print(f"✅ Kunci publik (n): {sc.n}")
    print(f"✅ Kunci privat (k): {sc.k}")
    print(f"✅ Nilai h: {sc.h}")
    
    while True:
        print("\n📝 Pilihan:")
        print("1. Masukkan pesan sendiri")
        print("2. Gunakan pesan contoh")
        print("3. Kembali ke menu utama")
        
        choice = input("\nPilih opsi (1-3): ").strip()
        
        if choice == "1":
            try:
                original_msg = int(input("Masukkan pesan rahasia (angka): "))
                cover_msg = int(input("Masukkan pesan samaran (angka): "))
            except ValueError:
                print("❌ Pesan harus berupa angka!")
                continue
                
        elif choice == "2":
            original_msg = random.randint(10000, 99999)
            cover_msg = random.randint(10000, 99999)
            print(f"📋 Pesan rahasia: {original_msg}")
            print(f"📋 Pesan samaran: {cover_msg}")
            
        elif choice == "3":
            return
            
        else:
            print("❌ Pilihan tidak valid!")
            continue
        
        print(f"\n🔄 Memproses komunikasi tersembunyi...")
        print(f"🤫 Pesan asli (rahasia): {original_msg}")
        print(f"👀 Pesan samaran (publik): {cover_msg}")
        
        try:
            # Buat pesan tersembunyi
            start_time = time.time()
            s1, s2, cover = sc.create_subliminal_message(original_msg, cover_msg)
            create_time = time.time() - start_time
            
            print(f"\n✅ Tanda tangan S1: {s1}")
            print(f"✅ Tanda tangan S2: {s2}")
            print(f"⏱️  Waktu pembuatan: {create_time:.6f} detik")
            
            # Simulasi perspektif pihak ketiga
            print(f"\n👁️  [PERSPEKTIF PIHAK KETIGA]")
            print(f"👀 Yang terlihat: {cover}")
            
            start_time = time.time()
            cover_valid = sc.verify_cover_message(cover, s1, s2)
            verify_time = time.time() - start_time
            
            print(f"🔍 Verifikasi pesan samaran: {'✅ VALID' if cover_valid else '❌ INVALID'}")
            print(f"⏱️  Waktu verifikasi: {verify_time:.6f} detik")
            print("💭 Status: Pihak ketiga hanya melihat pesan samaran")
            
            # Simulasi perspektif penerima sah
            print(f"\n🔓 [PERSPEKTIF PENERIMA SAH]")
            
            start_time = time.time()
            decrypted_msg = sc.decrypt_original_message(s1, s2)
            decrypt_time = time.time() - start_time
            
            print(f"🔓 Pesan yang didekripsi: {decrypted_msg}")
            print(f"✅ Dekripsi berhasil: {'Ya' if decrypted_msg == original_msg else 'Tidak'}")
            print(f"⏱️  Waktu dekripsi: {decrypt_time:.6f} detik")
            
            if decrypted_msg == original_msg:
                print("🎉 Sukses! Pesan rahasia berhasil dikomunikasikan secara tersembunyi!")
            else:
                print("❌ Error! Pesan tidak dapat didekripsi dengan benar!")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("💡 Tip: Pastikan pesan relatif prima dengan n")
        
        input("\n📱 Tekan Enter untuk melanjutkan...")


def generate_new_keys():
    """Generate kunci baru dengan berbagai ukuran"""
    print("\n🔑 GENERATE KUNCI BARU")
    print("="*50)
    
    key_sizes = [256, 512, 1024]
    
    print("📏 Pilih ukuran kunci:")
    for i, size in enumerate(key_sizes, 1):
        print(f"{i}. {size}-bit")
    print("4. Custom size")
    print("5. Kembali ke menu utama")
    
    choice = input("\nPilih opsi (1-5): ").strip()
    
    if choice == "5":
        return
    elif choice == "4":
        try:
            custom_size = int(input("Masukkan ukuran bit (128-2048): "))
            if custom_size < 128 or custom_size > 2048:
                print("❌ Ukuran harus antara 128-2048 bit!")
                return
            size = custom_size
        except ValueError:
            print("❌ Ukuran harus berupa angka!")
            return
    elif choice in ["1", "2", "3"]:
        size = key_sizes[int(choice) - 1]
    else:
        print("❌ Pilihan tidak valid!")
        return
    
    print(f"\n🔄 Membuat kunci {size}-bit...")
    print("⚠️  Ini mungkin membutuhkan waktu beberapa detik...")
    
    start_time = time.time()
    try:
        n, k, h = generate_keys(size)
        generation_time = time.time() - start_time
        
        print(f"\n✅ Kunci berhasil dibuat!")
        print(f"🔑 Kunci publik (n): {n}")
        print(f"🔐 Kunci privat (k): {k}")
        print(f"🧮 Nilai h: {h}")
        print(f"📏 Panjang n dalam bit: {n.bit_length()}")
        print(f"⏱️  Waktu pembuatan: {generation_time:.2f} detik")
        
        # Verifikasi kunci
        import math
        gcd_check = math.gcd(n, k)
        print(f"✅ Validitas kunci: GCD(n,k) = {gcd_check} {'✓' if gcd_check == 1 else '✗'}")
        
    except Exception as e:
        print(f"❌ Error dalam pembuatan kunci: {e}")
    
    input("\n📱 Tekan Enter untuk melanjutkan...")


def security_test():
    """Test keamanan sederhana"""
    print("\n🛡️  TEST KEAMANAN")
    print("="*50)
    
    print("🔄 Menjalankan test keamanan...")
    
    ds = DigitalSignature()
    message = 123456
    
    print(f"\n📋 Pesan test: {message}")
    s1, s2, r = ds.sign_message(message)
    print(f"✅ Tanda tangan asli: S1={s1}, S2={s2}")
    
    # Test 1: Modifikasi tanda tangan
    print("\n🧪 Test 1: Modifikasi tanda tangan")
    test_cases = [
        (s1 + 1, s2, "S1 dimodifikasi"),
        (s1, s2 + 1, "S2 dimodifikasi"),
        (s1 + 1, s2 + 1, "S1 dan S2 dimodifikasi")
    ]
    
    for mod_s1, mod_s2, description in test_cases:
        is_valid = ds.verify_signature(message, mod_s1, mod_s2)
        status = "❌ INVALID (Expected)" if not is_valid else "⚠️  VALID (Unexpected!)"
        print(f"   {description}: {status}")
    
    # Test 2: Modifikasi pesan
    print("\n🧪 Test 2: Modifikasi pesan")
    for i in range(1, 6):
        modified_msg = message + i
        is_valid = ds.verify_signature(modified_msg, s1, s2)
        status = "❌ INVALID (Expected)" if not is_valid else "⚠️  VALID (Unexpected!)"
        print(f"   Pesan {modified_msg}: {status}")
    
    # Test 3: Randomness
    print("\n🧪 Test 3: Randomness tanda tangan")
    signatures = []
    for i in range(3):
        s1_new, s2_new, r_new = ds.sign_message(message)
        signatures.append((s1_new, s2_new, r_new))
        print(f"   Tanda tangan {i+1}: r={r_new}")
    
    r_values = [sig[2] for sig in signatures]
    unique_r = len(set(r_values))
    print(f"   Unique r values: {unique_r}/3 {'✅' if unique_r > 1 else '⚠️'}")
    
    print("\n✅ Test keamanan selesai!")
    input("\n📱 Tekan Enter untuk melanjutkan...")


def benchmark_performance():
    """Benchmark performa algoritma"""
    print("\n⚡ BENCHMARK PERFORMA")
    print("="*50)
    
    print("🔄 Menjalankan benchmark...")
    
    # Test dengan berbagai ukuran kunci
    key_sizes = [256, 512]
    iterations = 10
    
    for size in key_sizes:
        print(f"\n📏 Testing dengan kunci {size}-bit:")
        
        # Generate kunci
        print("   🔑 Membuat kunci...")
        start_time = time.time()
        ds = DigitalSignature()
        key_time = time.time() - start_time
        print(f"   ⏱️  Waktu pembuatan kunci: {key_time:.4f} detik")
        
        # Test signing
        message = 123456
        sign_times = []
        verify_times = []
        
        for i in range(iterations):
            # Sign
            start_time = time.time()
            s1, s2, r = ds.sign_message(message + i)
            sign_time = time.time() - start_time
            sign_times.append(sign_time)
            
            # Verify
            start_time = time.time()
            is_valid = ds.verify_signature(message + i, s1, s2)
            verify_time = time.time() - start_time
            verify_times.append(verify_time)
        
        avg_sign = sum(sign_times) / len(sign_times)
        avg_verify = sum(verify_times) / len(verify_times)
        
        print(f"   📝 Rata-rata waktu signing: {avg_sign:.6f} detik")
        print(f"   🔍 Rata-rata waktu verifikasi: {avg_verify:.6f} detik")
        print(f"   🚀 Throughput signing: {1/avg_sign:.0f} ops/detik")
        print(f"   🚀 Throughput verifikasi: {1/avg_verify:.0f} ops/detik")
    
    print("\n✅ Benchmark selesai!")
    input("\n📱 Tekan Enter untuk melanjutkan...")


def show_help():
    """Tampilkan bantuan dan penjelasan"""
    print("\n❓ BANTUAN & PENJELASAN")
    print("="*50)
    
    help_text = """
🔐 ALGORITMA ONG-SCHNORR-SHAMIR

Algoritma ini memiliki dua skema utama:

1. 📝 DIGITAL SIGNATURE SCHEME
   • Untuk memastikan keaslian dan keutuhan pesan
   • Menggunakan pasangan kunci publik-privat
   • Proses: Sign → Verify

2. 🕵️  SUBLIMINAL CHANNEL SCHEME
   • Untuk menyembunyikan pesan rahasia dalam pesan samaran
   • Pihak ketiga hanya melihat pesan samaran
   • Penerima sah dapat mendekripsi pesan asli

🔑 KOMPONEN KUNCI:
   • n: kunci publik (bilangan prima besar)
   • k: kunci privat (relatif prima dengan n)
   • h: nilai yang dihitung dari k

⚡ KEAMANAN:
   • Menggunakan Miller-Rabin primality test
   • Modular arithmetic untuk operasi kriptografi
   • Random number generation untuk keamanan

💡 TIPS PENGGUNAAN:
   • Gunakan kunci minimal 512-bit untuk keamanan
   • Pesan harus berupa bilangan bulat
   • Untuk subliminal channel, pesan harus relatif prima dengan n

⚠️  CATATAN:
   • Implementasi ini untuk tujuan edukasi
   • Untuk produksi, diperlukan review keamanan mendalam
"""
    
    print(help_text)
    input("\n📱 Tekan Enter untuk kembali ke menu...")


def main():
    """Fungsi utama demo interaktif"""
    print_header()
    
    while True:
        print_menu()
        
        try:
            choice = input("Pilih menu (0-6): ").strip()
            
            if choice == "0":
                print("\n👋 Terima kasih telah menggunakan demo!")
                print("🌟 Jangan lupa beri star di GitHub: @HaikalE/ong-schnorr-shamir-algorithm")
                break
                
            elif choice == "1":
                demo_digital_signature()
                
            elif choice == "2":
                demo_subliminal_channel()
                
            elif choice == "3":
                generate_new_keys()
                
            elif choice == "4":
                security_test()
                
            elif choice == "5":
                benchmark_performance()
                
            elif choice == "6":
                show_help()
                
            else:
                print("❌ Pilihan tidak valid! Silakan pilih 0-6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            print("🔄 Kembali ke menu utama...")


if __name__ == "__main__":
    main()
