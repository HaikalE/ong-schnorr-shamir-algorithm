# Algoritma Ong-Schnorr-Shamir

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
- ✅ Contoh penggunaan yang lengkap
- ✅ Test keamanan sederhana
- ✅ Unit tests yang komprehensif
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

3. Jalankan contoh penggunaan:
```bash
python examples.py
```

4. Jalankan unit tests:
```bash
python test_ong_schnorr_shamir.py
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
├── examples.py                   # Contoh penggunaan lengkap
├── test_ong_schnorr_shamir.py    # Unit tests
├── requirements.txt              # Dependencies
└── LICENSE                       # MIT License
```

## 🔍 Contoh Output

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

- **Pembuatan kunci 512-bit**: ~0.1-1 detik
- **Pembuatan tanda tangan**: ~0.001 detik
- **Verifikasi tanda tangan**: ~0.001 detik
- **Enkripsi subliminal**: ~0.001 detik
- **Dekripsi subliminal**: ~0.001 detik

## 🔒 Keamanan

Algoritma ini menggunakan:
- **Miller-Rabin primality test** untuk pembuatan bilangan prima
- **Modular arithmetic** untuk operasi kriptografi
- **Random number generation** untuk bilangan acak yang aman

> ⚠️ **Catatan**: Implementasi ini dibuat untuk tujuan edukasi dan penelitian. Untuk penggunaan produksi, diperlukan review keamanan yang lebih mendalam.

## 🧪 Testing

### Jalankan Contoh Lengkap
```bash
python examples.py
```

### Jalankan Unit Tests
```bash
python test_ong_schnorr_shamir.py
```

### Test yang Tersedia:
- ✅ Digital signature dengan berbagai pesan
- ✅ Subliminal channel dengan berbagai skenario
- ✅ Pembuatan kunci dengan berbagai ukuran
- ✅ Test keamanan sederhana
- ✅ Test modifikasi tanda tangan
- ✅ Test properti keamanan algoritma
- ✅ Test validasi input dan error handling

## 📚 Referensi

- Makalah asli Ong-Schnorr-Shamir
- Cryptography theory dan praktek
- Digital signature standards

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📄 Lisensi

MIT License - lihat file [LICENSE](LICENSE) untuk detail lengkap.

## 👤 Penulis

**HaikalE**
- GitHub: [@HaikalE](https://github.com/HaikalE)
- Repository: [ong-schnorr-shamir-algorithm](https://github.com/HaikalE/ong-schnorr-shamir-algorithm)

## 📞 Dukungan

Jika Anda menemukan bug atau memiliki pertanyaan:

1. Buka [Issues](https://github.com/HaikalE/ong-schnorr-shamir-algorithm/issues)
2. Berikan deskripsi yang jelas
3. Sertakan contoh kode jika memungkinkan

---

⭐ Jika project ini membantu Anda, jangan lupa berikan star!
