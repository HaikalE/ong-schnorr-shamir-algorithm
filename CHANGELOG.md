# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-08-04 - MAJOR FIXES

### 🔧 Critical Bug Fixes
- **FIXED: Digital Signature S2 Formula** - Corrected from `(2k)^-1 * term` to `k * 2^-1 * term`
- **FIXED: Subliminal Channel Decryption** - Corrected formula from `w = S1 + k^-1 * S2` to `w = S1 - k^-1 * S2`
- **FIXED: Unit Tests** - Updated tests to verify correct implementation instead of providing false security
- **FIXED: Mathematical Correctness** - All algebraic formulas now mathematically sound

### ✅ What's Working Now
- ✅ **Digital Signature verification now PASSES**
- ✅ **Subliminal Channel decryption now WORKS**
- ✅ **Security tests properly detect tampering**
- ✅ **Mathematical properties are correct**

### 🔧 Code Improvements
- **Enhanced Error Handling**: Better validation and error messages
- **Improved Demo**: Added system status and better state management
- **Reduced Code Duplication**: Helper functions for common operations
- **Better Test Coverage**: Added mathematical property verification tests

### 📚 Documentation Updates
- **Updated Examples**: All examples now show working algorithm
- **Enhanced README**: Clear indication of fixes applied
- **Improved Comments**: Better explanation of mathematical formulas
- **Added Fix Indicators**: Clear markers showing corrected implementation

### ⚠️ Breaking Changes
- **Unit Test Updates**: Previous tests that passed with incorrect implementation will now properly fail
- **Formula Changes**: Mathematical formulas corrected (affects any external implementations)

### 🔍 Technical Details
**Digital Signature S2 Fix:**
```python
# BEFORE (INCORRECT):
inv_2k = pow(2 * self.k, -1, self.n)  # (2k)^-1
s2 = (inv_2k * term) % self.n

# AFTER (CORRECT):
inv_2 = pow(2, -1, self.n)           # 2^-1
s2 = (self.k * inv_2 * term) % self.n  # k * 2^-1 * term
```

**Subliminal Channel Decryption Fix:**
```python
# BEFORE (INCORRECT):
original_message = (s1 + (k_inv * s2)) % self.n  # w = S1 + k^-1 * S2

# AFTER (CORRECT):
original_message = (s1 - (k_inv * s2)) % self.n  # w = S1 - k^-1 * S2
```

### 🧪 Test Results After Fix
```
Digital Signature Tests: ✅ ALL PASS
Subliminal Channel Tests: ✅ ALL PASS
Security Tests: ✅ ALL PASS
Mathematical Property Tests: ✅ ALL PASS
Performance Tests: ✅ ALL PASS
```

---

## [1.0.0] - 2025-08-04 - Initial Release (Had Critical Bugs)

### ⚠️ Known Issues (FIXED in v1.0.1)
- ❌ Digital signature verification always failed
- ❌ Subliminal channel decryption returned wrong values
- ❌ Unit tests provided false security (testing incorrect implementation)

### Added
- 🎉 Initial release of Ong-Schnorr-Shamir algorithm implementation
- ✅ Complete Digital Signature Scheme implementation (had bugs)
- ✅ Complete Subliminal Channel Scheme implementation (had bugs)
- ✅ Automatic key generation with Miller-Rabin primality test
- ✅ Comprehensive examples and usage demonstrations
- ✅ Interactive demo script with user-friendly interface
- ✅ Unit tests covering all major functionality (tested wrong implementation)
- ✅ Security tests for signature validation
- ✅ Performance benchmarking tools
- ✅ GitHub Actions CI/CD pipeline
- ✅ Multi-platform compatibility (Linux, Windows, macOS)
- ✅ Multi-version Python support (3.7 - 3.11)
- ✅ Comprehensive documentation and README
- ✅ MIT License

### Features
- 🔐 **Digital Signature**: Sign and verify messages (had verification bug)
- 🕵️ **Subliminal Channel**: Hide secret messages (had decryption bug)
- 🔑 **Key Generation**: Automatic generation of secure keys
- ⚡ **Performance**: Optimized modular arithmetic operations
- 🛡️ **Security**: Built-in validation and error handling
- 🧪 **Testing**: Test suite (tested incorrect implementation)
- 📊 **Benchmarking**: Performance measurement tools
- 🎮 **Interactive Demo**: User-friendly interface

---

## [Unreleased]

### Planned Features
- [ ] Web-based interactive demo
- [ ] Additional key formats (PEM, JSON)
- [ ] Performance optimizations for large keys
- [ ] Docker containerization
- [ ] API server implementation
- [ ] Graphical user interface

---

## Migration Guide

### From v1.0.0 to v1.0.1

**If you used v1.0.0:**
1. **Update your code** - The core algorithm now works correctly
2. **Re-run tests** - Previous "passing" tests were testing incorrect implementation
3. **Verify results** - Digital signatures should now verify successfully
4. **Check subliminal** - Decryption should now return correct original messages

**What to expect:**
- ✅ **Digital signatures will now verify as VALID** (were INVALID before)
- ✅ **Subliminal channel decryption will return correct messages** (was wrong before)
- ✅ **Security tests will properly detect tampering** (may have missed issues before)

## Legend

- ✅ **Added**: New features
- 🔧 **Changed**: Changes in existing functionality  
- 🐛 **Fixed**: Bug fixes
- ❌ **Removed**: Removed features
- 🛡️ **Security**: Security improvements
- ⚠️ **Deprecated**: Soon-to-be removed features

## Links

- [Repository](https://github.com/HaikalE/ong-schnorr-shamir-algorithm)
- [Issues](https://github.com/HaikalE/ong-schnorr-shamir-algorithm/issues)
- [Releases](https://github.com/HaikalE/ong-schnorr-shamir-algorithm/releases)
