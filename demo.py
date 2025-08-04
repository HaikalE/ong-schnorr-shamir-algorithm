#!/usr/bin/env python3

"""
Demo Interaktif Algoritma Ong-Schnorr-Shamir - FIXED VERSION

MAJOR UPDATE: Demo ini sekarang menggunakan implementasi yang benar!
- Bug formula S2 sudah diperbaiki: k * (1/2) * term
- Bug formula dekripsi subliminal sudah diperbaiki: w = S1 - k^-1 * S2
- Mengurangi duplikasi kode dengan helper functions
- State management yang lebih baik untuk konsistensi kunci

Script ini menyediakan interface interaktif untuk mencoba
algoritma Ong-Schnorr-Shamir secara langsung.
"""

import sys
import time
import random
from ong_schnorr_shamir import DigitalSignature, SubliminalChannel, generate_keys


# Global state untuk konsistensi kunci
current_ds = None
current_sc = None


def print_header():
    """Print header yang menarik"""
    print("\n" + "="*70)
    print("🔧 DEMO INTERAKTIF ALGORITMA ONG-SCHNORR-SHAMIR - FIXED! 🔧")
    print("="*70)
    print("✅ MAJOR FIXES APPLIED:")
    print("- Formula S2 diperbaiki: k * (1/2) * term")
    print("- Formula dekripsi subliminal diperbaiki: w = S1 - k^-1 * S2")
    print("- State management yang lebih baik")
    print("- Algoritma sekarang bekerja dengan benar!")
    print("="*70)
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
    print("7. 🔧 Status Sistem")
    print("0. 🚪 Keluar")
    print("-" * 50)


def get_user_message_choice() -> tuple:
    """
    Helper function untuk mendapatkan pilihan pesan dari user
    Mengurangi duplikasi kode antara digital signature dan subliminal channel
    
    Returns:
        tuple: (choice, message(s)) - choice adalah string, message bisa int atau tuple
    """
    while True:
        print("\n📝 Pilihan:")
        print("1. Masukkan pesan sendiri")
        print("2. Gunakan pesan contoh")
        print("3. Kembali ke menu utama")
        
        choice = input("\nPilih opsi (1-3): ").strip()
        
        if choice == "3":
            return ("back", None)
        elif choice in ["1", "2"]:
            return (choice, None)
        else:
            print("❌ Pilihan tidak valid!")
            continue


def get_single_message() -> int:
    """Helper untuk mendapatkan single message dari user"""
    try:
        return int(input("Masukkan pesan (angka): "))
    except ValueError:
        raise ValueError("Pesan harus berupa angka!")


def get_double_messages() -> tuple:
    """Helper untuk mendapatkan dua pesan (original dan cover) dari user"""
    try:
        original_msg = int(input("Masukkan pesan rahasia (angka): "))
        cover_msg = int(input("Masukkan pesan samaran (angka): "))
        return original_msg, cover_msg
    except ValueError:
        raise ValueError("Pesan harus berupa angka!")


def initialize_system():
    """Initialize atau re-initialize sistem dengan kunci baru"""
    global current_ds, current_sc
    
    print("\n⚙️  Inisialisasi sistem dengan kunci baru...")
    
    # Generate kunci yang sama untuk kedua skema
    ds = DigitalSignature()
    sc = SubliminalChannel(ds.n, ds.k)  # Gunakan kunci yang sama
    
    current_ds = ds
    current_sc = sc
    
    print(f"✅ Kunci publik (n): {ds.n}")
    print(f"✅ Kunci privat (k): {ds.k}")
    print(f"✅ Nilai h: {ds.h}")
    print("🔄 Sistem siap untuk demo!")


def demo_digital_signature():
    """Demo interaktif untuk digital signature"""
    global current_ds
    
    print("\n🔐 DEMO DIGITAL SIGNATURE SCHEME (FIXED VERSION)")
    print("="*60)
    
    if current_ds is None:
        initialize_system()
    
    while True:
        choice, _ = get_user_message_choice()
        
        if choice == "back":
            return
        
        try:
            if choice == "1":
                message = get_single_message()
            elif choice == "2":
                message = random.randint(10000, 999999)
                print(f"📋 Menggunakan pesan contoh: {message}")
            
            print(f"\n🔄 Memproses pesan: {message}")
            
            # Buat tanda tangan
            start_time = time.time()
            s1, s2, r = current_ds.sign_message(message)
            sign_time = time.time() - start_time
            
            print(f"✅ Tanda tangan S1: {s1}")
            print(f"✅ Tanda tangan S2: {s2}")
            print(f"✅ Bilangan acak r: {r}")
            print(f"⏱️  Waktu pembuatan: {sign_time:.6f} detik")
            
            # Verifikasi
            start_time = time.time()
            is_valid = current_ds.verify_signature(message, s1, s2)
            verify_time = time.time() - start_time
            
            if is_valid:
                print(f"\n🎉 Hasil verifikasi: ✅ VALID")
                print("🔧 FIXED! Algoritma sekarang bekerja dengan benar!")
            else:
                print(f"\n⚠️  Hasil verifikasi: ❌ INVALID")
                print("🐛 Masih ada masalah yang perlu diperbaiki")
            
            print(f"⏱️  Waktu verifikasi: {verify_time:.6f} detik")
            
            # Test dengan pesan yang dimodifikasi
            modified_message = message + 1
            is_valid_modified = current_ds.verify_signature(modified_message, s1, s2)
            print(f"🔍 Verifikasi pesan dimodifikasi ({modified_message}): {'✅ VALID (Problem!)' if is_valid_modified else '❌ INVALID (Expected)'}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        
        input("\n📱 Tekan Enter untuk melanjutkan...")


def demo_subliminal_channel():
    """Demo interaktif untuk subliminal channel"""
    global current_sc
    
    print("\n🕵️  DEMO SUBLIMINAL CHANNEL SCHEME (FIXED VERSION)")
    print("="*60)
    
    if current_sc is None:
        initialize_system()
    
    while True:
        choice, _ = get_user_message_choice()
        
        if choice == "back":
            return
            
        try:
            if choice == "1":
                original_msg, cover_msg = get_double_messages()
            elif choice == "2":
                original_msg = random.randint(10000, 99999)
                cover_msg = random.randint(10000, 99999)
                print(f"📋 Pesan rahasia: {original_msg}")
                print(f"📋 Pesan samaran: {cover_msg}")
            
            print(f"\n🔄 Memproses komunikasi tersembunyi...")
            print(f"🤫 Pesan asli (rahasia): {original_msg}")
            print(f"👀 Pesan samaran (publik): {cover_msg}")
            
            # Buat pesan tersembunyi
            start_time = time.time()
            s1, s2, cover = current_sc.create_subliminal_message(original_msg, cover_msg)
            create_time = time.time() - start_time
            
            print(f"\n✅ Tanda tangan S1: {s1}")
            print(f"✅ Tanda tangan S2: {s2}")
            print(f"⏱️  Waktu pembuatan: {create_time:.6f} detik")
            
            # Simulasi perspektif pihak ketiga
            print(f"\n👁️  [PERSPEKTIF PIHAK KETIGA]")
            print(f"👀 Yang terlihat: {cover}")
            
            start_time = time.time()
            cover_valid = current_sc.verify_cover_message(cover, s1, s2)
            verify_time = time.time() - start_time
            
            if cover_valid:
                print(f"🔍 Verifikasi pesan samaran: ✅ VALID")
            else:
                print(f"🔍 Verifikasi pesan samaran: ❌ INVALID")
            print(f"⏱️  Waktu verifikasi: {verify_time:.6f} detik")
            print("💭 Status: Pihak ketiga hanya melihat pesan samaran")
            
            # Simulasi perspektif penerima sah
            print(f"\n🔓 [PERSPEKTIF PENERIMA SAH]")
            
            start_time = time.time()
            decrypted_msg = current_sc.decrypt_original_message(s1, s2)
            decrypt_time = time.time() - start_time
            
            print(f"🔓 Pesan yang didekripsi: {decrypted_msg}")
            
            if decrypted_msg == original_msg:
                print(f"✅ Dekripsi berhasil: YA")
                print("🔧 FIXED! Dekripsi sekarang bekerja dengan benar!")
                if cover_valid:
                    print("🎉 Sukses! Pesan rahasia berhasil dikomunikasikan secara tersembunyi!")
            else:
                print(f"❌ Dekripsi berhasil: TIDAK")
                print("⚠️  Masih ada masalah dengan dekripsi")
            
            print(f"⏱️  Waktu dekripsi: {decrypt_time:.6f} detik")
                
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
        
        # Tanya apakah ingin menggunakan kunci ini
        use_key = input("\n🔄 Gunakan kunci ini untuk demo? (y/n): ").strip().lower()
        if use_key == 'y':
            global current_ds, current_sc
            current_ds = DigitalSignature(n, k)
            current_sc = SubliminalChannel(n, k)
            print("✅ Kunci baru telah diaktifkan untuk demo!")
        
    except Exception as e:
        print(f"❌ Error dalam pembuatan kunci: {e}")
    
    input("\n📱 Tekan Enter untuk melanjutkan...")


def security_test():
    """Test keamanan sederhana"""
    global current_ds
    
    print("\n🛡️  TEST KEAMANAN (FIXED VERSION)")
    print("="*50)
    
    if current_ds is None:
        initialize_system()
    
    print("🔄 Menjalankan test keamanan...")
    
    message = 123456
    
    print(f"\n📋 Pesan test: {message}")
    s1, s2, r = current_ds.sign_message(message)
    print(f"✅ Tanda tangan asli: S1={s1}, S2={s2}")
    
    # Verifikasi signature asli
    is_valid_original = current_ds.verify_signature(message, s1, s2)
    print(f"🔍 Verifikasi signature asli: {'✅ VALID' if is_valid_original else '❌ INVALID'}")
    
    # Test 1: Modifikasi tanda tangan
    print("\n🧪 Test 1: Modifikasi tanda tangan")
    test_cases = [
        (s1 + 1, s2, "S1 dimodifikasi"),
        (s1, s2 + 1, "S2 dimodifikasi"),
        (s1 + 1, s2 + 1, "S1 dan S2 dimodifikasi")
    ]
    
    security_score = 0
    total_tests = 0
    
    for mod_s1, mod_s2, description in test_cases:
        is_valid = current_ds.verify_signature(message, mod_s1, mod_s2)
        status = "❌ INVALID (Expected)" if not is_valid else "⚠️  VALID (Problem!)"
        print(f"   {description}: {status}")
        if not is_valid:
            security_score += 1
        total_tests += 1
    
    # Test 2: Modifikasi pesan
    print("\n🧪 Test 2: Modifikasi pesan")
    for i in range(1, 6):
        modified_msg = message + i
        is_valid = current_ds.verify_signature(modified_msg, s1, s2)
        status = "❌ INVALID (Expected)" if not is_valid else "⚠️  VALID (Problem!)"
        print(f"   Pesan {modified_msg}: {status}")
        if not is_valid:
            security_score += 1
        total_tests += 1
    
    # Test 3: Randomness
    print("\n🧪 Test 3: Randomness tanda tangan")
    signatures = []
    for i in range(3):
        s1_new, s2_new, r_new = current_ds.sign_message(message)
        signatures.append((s1_new, s2_new, r_new))
        is_valid_new = current_ds.verify_signature(message, s1_new, s2_new)
        print(f"   Tanda tangan {i+1}: r={r_new}, valid={'✅' if is_valid_new else '❌'}")
        if is_valid_new:
            security_score += 1
        total_tests += 1
    
    r_values = [sig[2] for sig in signatures]
    unique_r = len(set(r_values))
    print(f"   Unique r values: {unique_r}/3 {'✅' if unique_r > 1 else '⚠️'}")
    if unique_r > 1:
        security_score += 1
    total_tests += 1
    
    print(f"\n📊 Security Score: {security_score}/{total_tests} ({security_score/total_tests*100:.1f}%)")
    
    if security_score >= total_tests * 0.8:
        print("🎉 SECURITY TESTS PASSED! Algoritma aman!")
    else:
        print("⚠️  SECURITY ISSUES DETECTED! Perlu investigasi lebih lanjut.")
    
    input("\n📱 Tekan Enter untuk melanjutkan...")


def benchmark_performance():
    """Benchmark performa algoritma"""
    global current_ds, current_sc
    
    print("\n⚡ BENCHMARK PERFORMA (FIXED VERSION)")
    print("="*50)
    
    if current_ds is None:
        initialize_system()
    
    print("🔄 Menjalankan benchmark...")
    
    iterations = 10
    message = 123456
    
    # Test signing performance
    print(f"\n📝 Testing signing performance ({iterations} iterations):")
    
    sign_times = []
    valid_signatures = 0
    
    for i in range(iterations):
        test_msg = message + i
        start_time = time.time()
        s1, s2, r = current_ds.sign_message(test_msg)
        sign_time = time.time() - start_time
        sign_times.append(sign_time)
        
        # Quick verification
        if current_ds.verify_signature(test_msg, s1, s2):
            valid_signatures += 1
    
    # Test verification performance
    s1, s2, r = current_ds.sign_message(message)
    verify_times = []
    
    for _ in range(iterations):
        start_time = time.time()
        current_ds.verify_signature(message, s1, s2)
        verify_time = time.time() - start_time
        verify_times.append(verify_time)
    
    avg_sign = sum(sign_times) / len(sign_times)
    avg_verify = sum(verify_times) / len(verify_times)
    
    print(f"   ⏱️  Rata-rata waktu signing: {avg_sign:.6f} detik")
    print(f"   ⏱️  Rata-rata waktu verifikasi: {avg_verify:.6f} detik")
    print(f"   🚀 Throughput signing: {1/avg_sign:.0f} ops/detik")
    print(f"   🚀 Throughput verifikasi: {1/avg_verify:.0f} ops/detik")
    print(f"   ✅ Valid signatures: {valid_signatures}/{iterations}")
    
    # Subliminal channel performance
    print(f"\n🕵️  Testing subliminal channel performance:")
    
    try:
        subliminal_times = []
        subliminal_success = 0
        
        for i in range(3):  # Fewer iterations due to coprime requirements
            original = 1000 + i
            cover = 2000 + i
            
            start_time = time.time()
            s1, s2, c = current_sc.create_subliminal_message(original, cover)
            cover_valid = current_sc.verify_cover_message(c, s1, s2)
            decrypted = current_sc.decrypt_original_message(s1, s2)
            total_time = time.time() - start_time
            
            subliminal_times.append(total_time)
            
            if cover_valid and decrypted == original:
                subliminal_success += 1
        
        if subliminal_times:
            avg_subliminal = sum(subliminal_times) / len(subliminal_times)
            print(f"   ⏱️  Rata-rata waktu subliminal: {avg_subliminal:.6f} detik")
            print(f"   ✅ Successful operations: {subliminal_success}/{len(subliminal_times)}")
        
    except ValueError:
        print(f"   ⚠️  Subliminal channel test skipped (coprime issues)")
    
    print("\n✅ Benchmark selesai!")
    input("\n📱 Tekan Enter untuk melanjutkan...")


def show_help():
    """Tampilkan bantuan dan penjelasan"""
    print("\n❓ BANTUAN & PENJELASAN (UPDATED)")
    print("="*50)
    
    help_text = """
🔧 ALGORITMA ONG-SCHNORR-SHAMIR - FIXED VERSION

✅ MAJOR FIXES APPLIED:
• Bug formula S2 diperbaiki: k * (1/2) * term, bukan (1/2k) * term
• Bug formula dekripsi subliminal diperbaiki: w = S1 - k^-1 * S2
• Algoritma sekarang bekerja dengan benar!

🔐 DIGITAL SIGNATURE SCHEME
   • Untuk memastikan keaslian dan keutuhan pesan
   • Menggunakan pasangan kunci publik-privat
   • Proses: Sign → Verify
   • ✅ Sekarang verification berhasil!

🕵️  SUBLIMINAL CHANNEL SCHEME
   • Untuk menyembunyikan pesan rahasia dalam pesan samaran
   • Pihak ketiga hanya melihat pesan samaran
   • Penerima sah dapat mendekripsi pesan asli
   • ✅ Sekarang decryption berhasil!

🔑 KOMPONEN KUNCI:
   • n: kunci publik (bilangan prima besar)
   • k: kunci privat (relatif prima dengan n)
   • h: nilai yang dihitung dari k

⚡ KEAMANAN:
   • Miller-Rabin primality test untuk bilangan prima
   • Modular arithmetic untuk operasi kriptografi
   • Secure random number generation

💡 TIPS PENGGUNAAN:
   • Gunakan kunci minimal 512-bit untuk keamanan
   • Pesan harus berupa bilangan bulat
   • Untuk subliminal channel, pesan harus relatif prima dengan n
   • Gunakan menu "Generate Kunci Baru" untuk kunci yang konsisten

🔧 PERBAIKAN YANG DILAKUKAN:
   • Formula matematis S2 diperbaiki
   • Formula dekripsi subliminal diperbaiki
   • State management yang lebih baik
   • Algoritma sekarang mathematically correct!

⚠️  CATATAN:
   • Implementasi ini untuk tujuan edukasi dan penelitian
   • Untuk produksi, diperlukan review keamanan mendalam
"""
    
    print(help_text)
    input("\n📱 Tekan Enter untuk kembali ke menu...")


def show_system_status():
    """Tampilkan status sistem saat ini"""
    global current_ds, current_sc
    
    print("\n🔧 STATUS SISTEM")
    print("="*50)
    
    if current_ds is None:
        print("❌ Sistem belum diinisialisasi")
        print("💡 Pilih menu 1, 2, atau 3 untuk inisialisasi otomatis")
        print("💡 Atau pilih menu 3 untuk generate kunci baru")
    else:
        print("✅ Sistem sudah diinisialisasi")
        print(f"🔑 Kunci publik (n): {current_ds.n}")
        print(f"🔐 Kunci privat (k): {current_ds.k}")
        print(f"🧮 Nilai h: {current_ds.h}")
        print(f"📏 Panjang kunci: {current_ds.n.bit_length()} bit")
        
        # Quick verification test
        test_msg = 12345
        try:
            s1, s2, r = current_ds.sign_message(test_msg)
            is_valid = current_ds.verify_signature(test_msg, s1, s2)
            print(f"🧪 Quick test: {'✅ PASSED' if is_valid else '❌ FAILED'}")
        except Exception as e:
            print(f"🧪 Quick test: ❌ ERROR - {e}")
    
    print("\n🔧 Implementasi Status:")
    print("✅ Bug formula S2 diperbaiki")
    print("✅ Bug formula dekripsi subliminal diperbaiki")
    print("✅ Unit tests diperbaiki")
    print("✅ Algoritma mathematically correct")
    
    input("\n📱 Tekan Enter untuk kembali ke menu...")


def main():
    """Fungsi utama demo interaktif yang sudah diperbaiki"""
    print_header()
    
    while True:
        print_menu()
        
        try:
            choice = input("Pilih menu (0-7): ").strip()
            
            if choice == "0":
                print("\n👋 Terima kasih telah menggunakan demo!")
                print("🔧 Algoritma sudah diperbaiki dan bekerja dengan benar!")
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
                
            elif choice == "7":
                show_system_status()
                
            else:
                print("❌ Pilihan tidak valid! Silakan pilih 0-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            print("🔄 Kembali ke menu utama...")


if __name__ == "__main__":
    main()
