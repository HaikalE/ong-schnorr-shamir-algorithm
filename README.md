# Algoritma Ong-Schnorr-Shamir

[![CI/CD Pipeline](https://github.com/HaikalE/ong-schnorr-shamir-algorithm/actions/workflows/ci.yml/badge.svg)](https://github.com/HaikalE/ong-schnorr-shamir-algorithm/actions/workflows/ci.yml)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/HaikalE/ong-schnorr-shamir-algorithm)

Implementasi lengkap algoritma Ong-Schnorr-Shamir dalam Python untuk **Digital Signature Scheme** dan **Subliminal Channel Scheme**.

## 📋 Deskripsi

Algoritma Ong-Schnorr-Shamir adalah algoritma kriptografi yang memiliki dua skema utama:

1. **Digital Signature Scheme**: Untuk menjaga keaslian dan keutuhan pesan
2. **Subliminal Channel Scheme**: Untuk menyembunyikan pesan rahasia di dalam pesan samaran

## 🚀 Fitur

- ✅ Implementasi lengkap Digital Signature Scheme
- ✅ Implementasi lengkap Subliminal Channel Scheme  
- ✅ Pembuatan kunci otomatis dengan berbagai ukuran
- ✅ Verifikasi tanda tangan digital
- ✅ Enkripsi dan dekripsi pesan tersembunyi
- ✅ Demo interaktif dengan interface user-friendly
- ✅ Contoh penggunaan yang lengkap
- ✅ Unit tests yang komprehensif
- ✅ Test keamanan dan performa
- ✅ CI/CD pipeline dengan GitHub Actions
- ✅ Multi-platform support (Windows, macOS, Linux)
- ✅ Multi-version Python support (3.7 - 3.11)
- ✅ Dokumentasi lengkap

## 📦 Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/HaikalE/ong-schnorr-shamir-algorithm.git
cd ong-schnorr-shamir-algorithm
```

2. Pastikan Python 3.7+ terinstall:
```bash
python --version
```

3. (Opsional) Buat virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 🎮 Quick Start

### 1. Demo Interaktif (Recommended)
```bash
python demo.py
```

### 2. Contoh Lengkap
```bash
python examples.py
```

### 3. Unit Tests
```bash
python test_ong_schnorr_shamir.py
```

### 4. Penggunaan Basic
```bash
python ong_schnorr_shamir.py
```

## 🔧 Penggunaan

### Digital Signature Scheme

```python
from ong_schnorr_shamir import DigitalSignature

# Inisialisasi
ds = DigitalSignature()

# Membuat tanda tangan
message = 12345
s1, s2, r = ds.sign_message(message)

# Verifikasi tanda tangan
is_valid = ds.verify_signature(message, s1, s2)
print(f"Verifikasi: {'Berhasil' if is_valid else 'Gagal'}")
```

### Subliminal Channel Scheme

```python
from ong_schnorr_shamir import SubliminalChannel

# Inisialisasi
sc = SubliminalChannel()

# Membuat pesan tersembunyi
original_message = 9876  # Pesan rahasia
cover_message = 5432     # Pesan samaran

s1, s2, cover = sc.create_subliminal_message(original_message, cover_message)

# Verifikasi oleh pihak ketiga (hanya melihat pesan samaran)
cover_valid = sc.verify_cover_message(cover, s1, s2)

# Dekripsi oleh penerima sah (mendapatkan pesan asli)
decrypted_message = sc.decrypt_original_message(s1, s2)

print(f"Pesan asli: {original_message}")
print(f"Pesan yang didekripsi: {decrypted_message}")
print(f"Dekripsi berhasil: {original_message == decrypted_message}")
```

## 🔐 Algoritma

### Digital Signature Scheme

1. **Penentuan Kunci**:
   - `n`: bilangan integer besar (kunci publik)
   - `k`: bilangan integer (kunci privat)
   - Syarat: `GCD(n,k) = 1` (relatif prima)

2. **Perhitungan nilai h**:
   ```
   h = -(k⁻¹)² mod n
   ```

3. **Pembuatan Tanda Tangan**:
   ```
   S1 = (1/2) * (M/r + r) mod n
   S2 = (1/2k) * (M/r - r) mod n
   ```

4. **Verifikasi**:
   ```
   S1² + h * S2² ≡ M (mod n)
   ```

### Subliminal Channel Scheme

1. **Pembuatan Pesan Tersembunyi**:
   ```
   S1 = (1/2) * (w'/w + w) mod n
   S2 = (1/2k) * (w'/w - w) mod n
   ```
   
2. **Verifikasi Pesan Samaran** (oleh pihak ketiga):
   ```
   S1² + h * S2² ≡ w' (mod n)
   ```

3. **Dekripsi Pesan Asli** (oleh penerima sah):
   ```
   w = S1 + k⁻¹ * S2
   ```

## 📁 Struktur File

```
ong-schnorr-shamir-algorithm/
├── README.md                      # Dokumentasi utama
├── ong_schnorr_shamir.py         # Implementasi algoritma
├── demo.py                       # Demo interaktif
├── examples.py                   # Contoh penggunaan lengkap
├── test_ong_schnorr_shamir.py    # Unit tests
├── requirements.txt              # Dependencies
├── LICENSE                       # MIT License
├── CHANGELOG.md                  # Version history
├── CONTRIBUTING.md               # Contributing guidelines
└── .github/
    └── workflows/
        └── ci.yml               # GitHub Actions CI/CD
```

## 🔍 Contoh Output

### Demo Interaktif
```
🔐 DEMO INTERAKTIF ALGORITMA ONG-SCHNORR-SHAMIR 🔐
==================================================================

📋 MENU UTAMA:
1. 📝 Demo Digital Signature Scheme
2. 🔍 Demo Subliminal Channel Scheme
3. 🔑 Generate Kunci Baru
4. 🧪 Test Keamanan
5. 📊 Benchmark Performa
6. ❓ Bantuan & Penjelasan
0. 🚪 Keluar
```

### Digital Signature
```
=== Digital Signature Scheme ===
Kunci publik (n): 1234567890123456789
Kunci privat (k): 987654321
Pesan: 12345
Tanda tangan S1: 456789123
Tanda tangan S2: 789123456
Verifikasi: ✓ VALID
```

### Subliminal Channel
```
=== Subliminal Channel Scheme ===
Pesan asli (rahasia): 9876
Pesan samaran (publik): 5432

[Perspektif Pihak Ketiga]
Pesan yang terlihat: 5432
Verifikasi pesan samaran: ✓ VALID

[Perspektif Penerima Sah]
Pesan yang didekripsi: 9876
Dekripsi berhasil: ✓ Ya
```

## ⚡ Performa

| Operasi | Waktu (512-bit) | Throughput |
|---------|----------------|------------|
| Pembuatan kunci | ~0.1-1 detik | - |
| Pembuatan signature | ~0.001 detik | ~1000 ops/sec |
| Verifikasi signature | ~0.001 detik | ~1000 ops/sec |
| Enkripsi subliminal | ~0.001 detik | ~1000 ops/sec |
| Dekripsi subliminal | ~0.001 detik | ~1000 ops/sec |

## 🔒 Keamanan

Algoritma ini menggunakan:
- **Miller-Rabin primality test** untuk pembuatan bilangan prima
- **Modular arithmetic** untuk operasi kriptografi
- **Cryptographically secure random number generation**
- **Input validation** dan error handling yang komprehensif

> ⚠️ **Catatan**: Implementasi ini dibuat untuk tujuan edukasi dan penelitian. Untuk penggunaan produksi, diperlukan review keamanan yang lebih mendalam.

## 🧪 Testing

### Jalankan Semua Tests
```bash
# Unit tests
python test_ong_schnorr_shamir.py

# Contoh lengkap  
python examples.py

# Demo interaktif
python demo.py
```

### GitHub Actions CI/CD

Repository ini dilengkapi dengan GitHub Actions yang otomatis menjalankan:

- ✅ **Unit tests** pada multiple Python versions (3.7-3.11)
- ✅ **Cross-platform testing** (Ubuntu, Windows, macOS)  
- ✅ **Security tests** untuk validasi algoritma
- ✅ **Performance benchmarks** untuk regression testing
- ✅ **Code quality checks** dengan linting

### Test Coverage

- ✅ Digital signature dengan berbagai pesan
- ✅ Subliminal channel dengan berbagai skenario
- ✅ Pembuatan kunci dengan berbagai ukuran
- ✅ Test keamanan dan modifikasi signature
- ✅ Test properti matematika algoritma
- ✅ Test validasi input dan error handling
- ✅ Test performa dan throughput

## 📚 Referensi

- Makalah asli Ong-Schnorr-Shamir algorithm
- Handbook of Applied Cryptography
- Digital signature standards dan best practices
- Modern cryptography theory dan implementation

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan baca [CONTRIBUTING.md](CONTRIBUTING.md) untuk panduan lengkap.

**Quick steps:**
1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/amazing-feature`)
3. Commit perubahan (`git commit -m 'Add amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buat Pull Request

### Types of Contributions Needed

- 🐛 **Bug fixes** dan improvements
- ✨ **New features** dan enhancements  
- 📚 **Documentation** improvements
- 🧪 **Additional tests** dan benchmarks
- 🔧 **Performance optimizations**
- 🌐 **Internationalization** (i18n)

## 📄 Lisensi

MIT License - lihat file [LICENSE](LICENSE) untuk detail lengkap.

## 📝 Changelog

Lihat [CHANGELOG.md](CHANGELOG.md) untuk riwayat perubahan dan versi.

## 👤 Penulis

**HaikalE**
- GitHub: [@HaikalE](https://github.com/HaikalE)
- Repository: [ong-schnorr-shamir-algorithm](https://github.com/HaikalE/ong-schnorr-shamir-algorithm)

## 📞 Dukungan

### Mendapatkan Bantuan

- 📖 **Dokumentasi**: Baca README dan file dokumentasi
- 💬 **Discussions**: Untuk pertanyaan umum dan diskusi
- 🐛 **Issues**: Untuk bug reports dan feature requests
- 💼 **Email**: Untuk security issues (private)

### Melaporkan Issues

1. Cek [existing issues](https://github.com/HaikalE/ong-schnorr-shamir-algorithm/issues) terlebih dahulu
2. Gunakan template yang tersedia
3. Berikan informasi yang lengkap:
   - Python version dan OS
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages atau stack traces

### Security Issues

Untuk security vulnerabilities, jangan buat public issue. Email maintainer secara langsung dengan detail lengkap.

---

## 🌟 Showcase

### Badge untuk README Anda

Jika Anda menggunakan algoritma ini dalam project Anda:

```markdown
[![Powered by Ong-Schnorr-Shamir](https://img.shields.io/badge/Powered%20by-Ong--Schnorr--Shamir-blue)](https://github.com/HaikalE/ong-schnorr-shamir-algorithm)
```

### Citation

Jika Anda menggunakan implementasi ini dalam penelitian:

```bibtex
@software{ong_schnorr_shamir_2025,
  author = {HaikalE},
  title = {Ong-Schnorr-Shamir Algorithm Implementation},
  url = {https://github.com/HaikalE/ong-schnorr-shamir-algorithm},
  year = {2025}
}
```

---

⭐ **Jika project ini membantu Anda, jangan lupa berikan star!** ⭐

**Terima kasih telah menggunakan Ong-Schnorr-Shamir Algorithm! 🚀**
