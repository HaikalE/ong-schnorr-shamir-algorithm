---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: HaikalE

---

## 🐛 Bug Description
A clear and concise description of what the bug is.

## 🔄 Steps to Reproduce
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## ✅ Expected Behavior
A clear and concise description of what you expected to happen.

## ❌ Actual Behavior
A clear and concise description of what actually happened.

## 📱 Environment
 - OS: [e.g. Windows 10, macOS 12.1, Ubuntu 20.04]
 - Python Version: [e.g. 3.9.7]
 - Repository Version: [e.g. v1.0.1]

## 📝 Code Sample
If applicable, add a minimal code sample to reproduce the issue:

```python
from ong_schnorr_shamir import DigitalSignature

# Your code here that reproduces the bug
ds = DigitalSignature()
# ...
```

## 📊 Test Results
If you ran the tests, please include the output:

```bash
# Output of python test_ong_schnorr_shamir.py
```

## 🖼️ Screenshots
If applicable, add screenshots to help explain your problem.

## 🤔 Additional Context
Add any other context about the problem here.

## ✅ Checklist
- [ ] I have read the [README.md](../README.md)
- [ ] I have checked that this issue hasn't been reported before
- [ ] I have tried running `python examples.py` and `python demo.py`
- [ ] I have included a minimal code sample that reproduces the issue
- [ ] I have included my environment information

## 🔧 For Algorithm Issues
If this is related to the core algorithm:

- [ ] Digital Signature verification fails when it should pass
- [ ] Subliminal Channel decryption returns wrong values
- [ ] Mathematical formulas seem incorrect
- [ ] Security tests show unexpected results

**Note**: Major algorithm bugs were fixed in v1.0.1. If you're experiencing algorithm issues, please make sure you're using the latest version.
