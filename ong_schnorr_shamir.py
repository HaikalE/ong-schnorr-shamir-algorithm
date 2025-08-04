import random
import math
from typing import Tuple, Optional


class OngSchnorrShamir:
    """
    Implementasi Algoritma Ong-Schnorr-Shamir untuk:
    1. Digital Signature Scheme
    2. Subliminal Channel Scheme
    """
    
    def __init__(self, n: int = None, k: int = None):
        """
        Inisialisasi dengan parameter n dan k
        
        Args:
            n: Bilangan integer besar (kunci publik)
            k: Bilangan integer (kunci privat)
        """
        if n is None:
            n = self._generate_large_prime()
        if k is None:
            k = self._generate_coprime(n)
            
        self.n = n  # Kunci publik
        self.k = k  # Kunci privat
        
        # Pastikan n dan k relatif prima
        if math.gcd(n, k) != 1:
            raise ValueError("n dan k harus relatif prima (GCD(n,k) = 1)")
        
        # Hitung nilai h
        self.h = self._calculate_h()
    
    def _generate_large_prime(self, bits: int = 512) -> int:
        """
        Generate bilangan prima besar
        """
        while True:
            num = random.getrandbits(bits)
            if self._is_prime(num):
                return num
    
    def _is_prime(self, n: int, k: int = 5) -> bool:
        """
        Miller-Rabin primality test
        """
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        
        # Tulis n-1 sebagai d * 2^r
        r = 0
        d = n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        
        # Miller-Rabin test
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    
    def _generate_coprime(self, n: int) -> int:
        """
        Generate bilangan yang relatif prima dengan n
        """
        while True:
            k = random.randint(2, n - 1)
            if math.gcd(n, k) == 1:
                return k
    
    def _calculate_h(self) -> int:
        """
        Hitung nilai h = -(k^-1)^2 mod n
        """
        k_inv = pow(self.k, -1, self.n)  # Modular inverse of k
        h = (-(k_inv ** 2)) % self.n
        return h
    
    def _generate_random_coprime(self, n: int) -> int:
        """
        Generate bilangan acak yang relatif prima dengan n
        """
        while True:
            r = random.randint(2, n - 1)
            if math.gcd(n, r) == 1:
                return r


class DigitalSignature(OngSchnorrShamir):
    """
    Implementasi skema tanda tangan digital Ong-Schnorr-Shamir
    """
    
    def sign_message(self, message: int) -> Tuple[int, int, int]:
        """
        Membuat tanda tangan digital untuk pesan
        
        Args:
            message: Pesan yang akan ditandatangani (M)
            
        Returns:
            Tuple berisi (S1, S2, r)
        """
        # Generate bilangan acak r
        r = self._generate_random_coprime(self.n)
        
        # Hitung S1 dan S2
        try:
            # S1 = (1/2) * (M/r + r) mod n
            inv_2 = pow(2, -1, self.n)  # Modular inverse of 2
            inv_r = pow(r, -1, self.n)  # Modular inverse of r
            
            s1 = (inv_2 * ((message * inv_r) + r)) % self.n
            
            # S2 = (1/(2k)) * (M/r - r) mod n
            inv_2k = pow(2 * self.k, -1, self.n)  # Modular inverse of 2k
            s2 = (inv_2k * ((message * inv_r) - r)) % self.n
            
            return s1, s2, r
            
        except ValueError as e:
            raise ValueError(f"Error dalam perhitungan tanda tangan: {e}")
    
    def verify_signature(self, message: int, s1: int, s2: int) -> bool:
        """
        Verifikasi tanda tangan digital
        
        Args:
            message: Pesan asli (M)
            s1: Tanda tangan S1
            s2: Tanda tangan S2
            
        Returns:
            True jika verifikasi berhasil, False sebaliknya
        """
        try:
            # Verifikasi: S1^2 + h * S2^2 ≡ M (mod n)
            left_side = (pow(s1, 2, self.n) + (self.h * pow(s2, 2, self.n))) % self.n
            return left_side == message % self.n
            
        except Exception:
            return False


class SubliminalChannel(OngSchnorrShamir):
    """
    Implementasi skema saluran tersembunyi (subliminal channel) Ong-Schnorr-Shamir
    """
    
    def create_subliminal_message(self, original_message: int, cover_message: int) -> Tuple[int, int, int]:
        """
        Membuat pesan tersembunyi dengan saluran subliminal
        
        Args:
            original_message: Pesan asli yang akan disembunyikan (w)
            cover_message: Pesan samaran (w')
            
        Returns:
            Tuple berisi (S1, S2, cover_message)
        """
        # Pastikan kedua pesan relatif prima dengan n
        if math.gcd(original_message, self.n) != 1:
            raise ValueError("Pesan asli harus relatif prima dengan n")
        if math.gcd(cover_message, self.n) != 1:
            raise ValueError("Pesan samaran harus relatif prima dengan n")
        
        try:
            # S1 = (1/2) * (w'/w + w) mod n
            inv_2 = pow(2, -1, self.n)
            inv_w = pow(original_message, -1, self.n)
            
            s1 = (inv_2 * ((cover_message * inv_w) + original_message)) % self.n
            
            # S2 = (1/(2k)) * (w'/w - w) mod n
            inv_2k = pow(2 * self.k, -1, self.n)
            s2 = (inv_2k * ((cover_message * inv_w) - original_message)) % self.n
            
            return s1, s2, cover_message
            
        except ValueError as e:
            raise ValueError(f"Error dalam pembuatan pesan tersembunyi: {e}")
    
    def verify_cover_message(self, cover_message: int, s1: int, s2: int) -> bool:
        """
        Verifikasi pesan samaran (oleh pihak ketiga)
        
        Args:
            cover_message: Pesan samaran (w')
            s1: Tanda tangan S1
            s2: Tanda tangan S2
            
        Returns:
            True jika verifikasi berhasil, False sebaliknya
        """
        try:
            # Verifikasi: S1^2 + h * S2^2 ≡ w' (mod n)
            left_side = (pow(s1, 2, self.n) + (self.h * pow(s2, 2, self.n))) % self.n
            return left_side == cover_message % self.n
            
        except Exception:
            return False
    
    def decrypt_original_message(self, s1: int, s2: int) -> int:
        """
        Dekripsi untuk mendapatkan pesan asli (oleh penerima sah)
        
        Args:
            s1: Tanda tangan S1
            s2: Tanda tangan S2
            
        Returns:
            Pesan asli (w)
        """
        try:
            # w = S1 + k^-1 * S2
            k_inv = pow(self.k, -1, self.n)
            original_message = (s1 + (k_inv * s2)) % self.n
            
            return original_message
            
        except ValueError as e:
            raise ValueError(f"Error dalam dekripsi pesan asli: {e}")


def generate_keys(bits: int = 512) -> Tuple[int, int, int]:
    """
    Generate kunci untuk algoritma Ong-Schnorr-Shamir
    
    Args:
        bits: Panjang bit untuk kunci
        
    Returns:
        Tuple berisi (n, k, h) dimana:
        - n: kunci publik
        - k: kunci privat
        - h: nilai h yang dihitung
    """
    oss = OngSchnorrShamir()
    return oss.n, oss.k, oss.h


if __name__ == "__main__":
    # Contoh penggunaan sederhana
    print("=== Ong-Schnorr-Shamir Algorithm Demo ===")
    print("\n1. Digital Signature Scheme:")
    
    # Digital Signature
    ds = DigitalSignature()
    message = 12345
    
    print(f"Kunci publik (n): {ds.n}")
    print(f"Kunci privat (k): {ds.k}")
    print(f"Nilai h: {ds.h}")
    print(f"Pesan: {message}")
    
    # Sign message
    s1, s2, r = ds.sign_message(message)
    print(f"Tanda tangan S1: {s1}")
    print(f"Tanda tangan S2: {s2}")
    print(f"Bilangan acak r: {r}")
    
    # Verify signature
    is_valid = ds.verify_signature(message, s1, s2)
    print(f"Verifikasi: {'Berhasil' if is_valid else 'Gagal'}")
    
    print("\n2. Subliminal Channel Scheme:")
    
    # Subliminal Channel
    sc = SubliminalChannel()
    original_msg = 9876
    cover_msg = 5432
    
    print(f"Pesan asli (w): {original_msg}")
    print(f"Pesan samaran (w'): {cover_msg}")
    
    # Create subliminal message
    s1_sub, s2_sub, cover = sc.create_subliminal_message(original_msg, cover_msg)
    print(f"Tanda tangan S1: {s1_sub}")
    print(f"Tanda tangan S2: {s2_sub}")
    
    # Verify cover message (by third party)
    cover_valid = sc.verify_cover_message(cover, s1_sub, s2_sub)
    print(f"Verifikasi pesan samaran: {'Berhasil' if cover_valid else 'Gagal'}")
    
    # Decrypt original message (by legitimate receiver)
    decrypted_msg = sc.decrypt_original_message(s1_sub, s2_sub)
    print(f"Pesan asli yang didekripsi: {decrypted_msg}")
    print(f"Dekripsi berhasil: {'Ya' if decrypted_msg == original_msg else 'Tidak'}")
