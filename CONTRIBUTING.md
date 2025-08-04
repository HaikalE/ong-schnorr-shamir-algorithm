# Contributing to Ong-Schnorr-Shamir Algorithm

🎉 Thank you for your interest in contributing to this project! This guide will help you get started.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Issue Guidelines](#issue-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code:

- **Be respectful** and inclusive
- **Be collaborative** and supportive
- **Focus on what is best** for the community
- **Show empathy** towards other community members

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ong-schnorr-shamir-algorithm.git
   cd ong-schnorr-shamir-algorithm
   ```

3. Add the original repository as upstream:
   ```bash
   git remote add upstream https://github.com/HaikalE/ong-schnorr-shamir-algorithm.git
   ```

## Development Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   # Optional: Install development tools
   pip install pytest black flake8 mypy
   ```

3. **Verify installation**:
   ```bash
   python ong_schnorr_shamir.py
   python test_ong_schnorr_shamir.py
   ```

## Making Changes

### 1. Create a Branch

Always create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
# or  
git checkout -b docs/documentation-update
```

### 2. Make Your Changes

- **Core algorithm changes**: Modify `ong_schnorr_shamir.py`
- **Examples**: Update `examples.py` or `demo.py`
- **Tests**: Add/modify tests in `test_ong_schnorr_shamir.py`
- **Documentation**: Update `README.md`, docstrings, or create new docs

### 3. Follow Coding Standards

See [Coding Standards](#coding-standards) section below.

## Testing

### Running Tests

```bash
# Run all tests
python test_ong_schnorr_shamir.py

# Run specific test class
python -m unittest test_ong_schnorr_shamir.TestDigitalSignature -v

# Run with coverage (if installed)
coverage run test_ong_schnorr_shamir.py
coverage report -m
```

### Test Types

1. **Unit Tests**: Test individual functions and methods
2. **Integration Tests**: Test complete workflows
3. **Security Tests**: Verify security properties
4. **Performance Tests**: Benchmark performance

### Writing New Tests

When adding new features, please include tests:

```python
class TestNewFeature(unittest.TestCase):
    def setUp(self):
        """Setup for each test"""
        self.instance = YourClass()
    
    def test_new_functionality(self):
        """Test description"""
        # Arrange
        input_data = "test_input"
        expected = "expected_output"
        
        # Act
        result = self.instance.new_method(input_data)
        
        # Assert
        self.assertEqual(result, expected)
```

## Submitting Changes

### 1. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add: New feature for key export functionality

- Implement PEM format export
- Add JSON format support  
- Include comprehensive tests
- Update documentation

Closes #123"
```

**Commit Message Format:**
- **Type**: Add, Fix, Update, Remove, etc.
- **Brief description** (50 chars max)
- **Blank line**
- **Detailed description** if needed
- **Issue references** (Closes #123, Fixes #456)

### 2. Push and Create Pull Request

```bash
git push origin your-branch-name
```

Then create a Pull Request on GitHub with:

- **Clear title** describing the change
- **Detailed description** of what and why
- **References to issues** if applicable
- **Screenshots** if UI changes
- **Testing notes** for complex changes

### 3. Pull Request Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review of code completed
- [ ] Tests added/updated and passing
- [ ] Documentation updated if needed
- [ ] No breaking changes (or clearly documented)
- [ ] Changelog updated for significant changes

## Coding Standards

### Python Style

- **PEP 8** compliance
- **Type hints** for public APIs
- **Docstrings** for all public functions/classes
- **Clear variable names** and comments

```python
def sign_message(self, message: int) -> Tuple[int, int, int]:
    """
    Create digital signature for a message.
    
    Args:
        message: The message to be signed (integer)
        
    Returns:
        Tuple containing (S1, S2, r) signature components
        
    Raises:
        ValueError: If message is invalid
    """
    # Implementation here...
```

### Code Organization

- **Small functions**: Single responsibility
- **Clear abstractions**: Well-defined interfaces
- **Error handling**: Appropriate exceptions
- **Performance**: Consider algorithmic complexity

### Security Considerations

- **Input validation**: Always validate inputs
- **Secure randomness**: Use cryptographically secure RNG
- **Constant-time operations**: Where applicable
- **Memory safety**: Clear sensitive data when possible

## Issue Guidelines

### Reporting Bugs

Use the bug report template and include:

- **Python version** and OS
- **Steps to reproduce** the issue
- **Expected vs actual** behavior
- **Error messages** or stack traces
- **Minimal code example** if possible

### Feature Requests

Describe:

- **Use case**: Why is this needed?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches?
- **Additional context**: Any relevant information

### Security Issues

For security vulnerabilities:

1. **DO NOT** open a public issue
2. **Email** the maintainer directly
3. **Include** detailed reproduction steps
4. **Wait** for confirmation before disclosure

## Types of Contributions

We welcome various types of contributions:

### 🐛 Bug Fixes
- Fix reported issues
- Improve error handling
- Address edge cases

### ✨ New Features
- Algorithm improvements
- New functionality
- Performance optimizations

### 📚 Documentation
- README improvements
- Code comments
- Example updates
- Tutorial creation

### 🧪 Testing
- Additional test cases
- Performance benchmarks
- Security tests
- Edge case coverage

### 🔧 Infrastructure
- CI/CD improvements
- Build system updates
- Dependency management
- Development tools

## Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **CHANGELOG.md** for significant contributions
- **GitHub** contributors page
- **Releases** acknowledgments

## Questions?

- **General questions**: Open a discussion
- **Bug reports**: Create an issue
- **Feature requests**: Create an issue  
- **Security issues**: Email maintainer
- **Contributing help**: Ask in discussions

---

## Quick Start Checklist

For new contributors:

- [ ] Read this contributing guide
- [ ] Fork and clone the repository
- [ ] Set up development environment
- [ ] Run existing tests to verify setup
- [ ] Create a branch for your changes
- [ ] Make small, focused changes
- [ ] Add tests for new functionality
- [ ] Ensure all tests pass
- [ ] Submit a pull request
- [ ] Respond to review feedback

**Thank you for contributing! 🚀**

Your contributions help make this project better for everyone in the cryptography and computer science community.
