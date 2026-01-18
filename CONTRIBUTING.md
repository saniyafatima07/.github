# Contributing to pointblank-club

Welcome to the pointblank-club organization! This document provides unified contribution guidelines that apply across all our repositories. Thank you for your interest in contributing to our projects.

## Our Projects

| Repository | Description | Language |
|------------|-------------|----------|
| [kettle](https://github.com/pointblank-club/kettle) | Minimal Container Runtime Engine | Go |
| [vestigo](https://github.com/pointblank-club/vestigo) | Firmware Analysis and Crypto-Detection Pipeline | Python |
| [oaas](https://github.com/pointblank-club/oaas) | Obfuscation As A Service - LLVM Binary Obfuscator | Python |
| [syshardn](https://github.com/pointblank-club/syshardn) | Multi-Platform System Hardening Tool | Python |
| [IRIS](https://github.com/pointblank-club/IRIS) | ML-Guided RISC-V Compiler Optimization | C/Python |
| [edgeFlow](https://github.com/pointblank-club/edgeFlow) | DSL for Optimizing ML Models on Edge Devices | Python |

## Code of Conduct

All contributors are expected to:

- Be respectful and inclusive in all interactions
- Welcome diverse perspectives and constructive feedback
- Act professionally in community discussions
- Help create a positive environment for newcomers

By participating in any pointblank-club project, you agree to uphold these principles.

## Getting Started

### 1. Explore the Repository

Before contributing to any project:

- Read the repository's README to understand its goals and architecture
- Review existing issues and pull requests to see ongoing work
- Check the repository-specific CONTRIBUTING.md for project-specific guidelines

### 2. Fork and Clone

```bash
git clone https://github.com/<your-username>/<repository>.git
cd <repository>
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names that reflect the change you're making.

## Development Setup

### Python Projects (vestigo, oaas, syshardn, IRIS, edgeFlow)

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # if available

# Install the package in editable mode (if applicable)
pip install -e .
```

### Go Projects (kettle)

```bash
# Ensure Go is installed
go version

# Download dependencies
go mod download

# Build
go build ./...
```

## Code Style Guidelines

### Python

- Follow PEP 8 style guidelines
- Use `black` for code formatting
- Use `isort` for import sorting
- Use `flake8` for linting
- Use `mypy` for type checking where applicable
- Keep functions small and well-documented
- Include docstrings for public APIs

```bash
# Format code
black src/ tests/
isort src/ tests/

# Lint
flake8 src/ tests/

# Type check
mypy src/ --ignore-missing-imports
```

### Go

- Follow standard Go conventions and idioms
- Use `gofmt` for formatting
- Keep code readable and well-commented
- Follow existing patterns in the codebase

### Commit Messages

Use conventional commit format for clear history:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `ci`: CI/CD changes
- `chore`: Maintenance tasks

Examples:
```
feat(compiler): add support for new optimization pass
fix(parser): handle edge case in config parsing
docs: update installation instructions
refactor(core): simplify validation logic
```

## Testing Guidelines

### Running Tests

**Python projects:**
```bash
pytest tests/
pytest tests/ --cov=<package> --cov-report=term  # with coverage
```

**Go projects:**
```bash
go test ./...
```

### Writing Tests

- Add tests for new functionality
- Update tests when modifying existing behavior
- Include both positive and negative test cases
- Aim for meaningful coverage of critical paths

## Pull Request Process

### Before Submitting

1. Ensure your branch is up to date with `main`
2. Run all tests and ensure they pass
3. Run linters and formatters
4. Update documentation if needed
5. Keep changes focused and scoped

### Submitting a PR

1. Push your changes to your fork
2. Open a pull request against `main`
3. Provide a clear description including:
   - What the change does
   - Why it's needed
   - Any relevant issues (e.g., `Fixes #123`)
   - Manual verification steps if applicable

### PR Best Practices

- Keep PRs small and focused on a single concern
- Write clear commit messages
- Respond to review feedback promptly
- Be open to suggestions and improvements
- Avoid mixing refactors with behavior changes

## Ways to Contribute

### Code Contributions

- Implement new features or enhancements
- Fix bugs or performance issues
- Improve code quality and maintainability
- Add or improve tests

### Non-Code Contributions

- **Documentation**: Fix typos, improve clarity, add examples
- **Issue Triage**: Help label, reproduce, or clarify issues
- **Community Support**: Answer questions, help newcomers
- **Design**: Suggest improvements to APIs or workflows

## Issues and Feature Requests

### Reporting Bugs

Include:
- Clear summary and steps to reproduce
- Expected vs actual behavior
- Environment details (OS, language version, etc.)
- Relevant error messages or logs

### Feature Requests

Include:
- Description of the problem or limitation
- Proposed solution or approach
- How it fits with existing architecture

## Finding Work

Look for issues labeled:
- `good first issue` - Beginner-friendly tasks
- `help wanted` - Tasks needing additional contributors

If you plan to work on an issue, comment on it to avoid duplicate effort.

## Security

If you discover a security vulnerability:
- Do not open a public issue
- Contact maintainers directly or use private disclosure
- Allow time for the issue to be addressed before any public discussion

## Repository-Specific Guidelines

Each repository may have additional guidelines in its own CONTRIBUTING.md:

- [kettle CONTRIBUTING.md](https://github.com/pointblank-club/kettle/blob/main/CONTRIBUTING.md)
- [vestigo CONTRIBUTING.md](https://github.com/pointblank-club/vestigo/blob/main/CONTRIBUTING.md)
- [oaas CONTRIBUTING.md](https://github.com/pointblank-club/oaas/blob/main/CONTRIBUTING.md)
- [syshardn CONTRIBUTING.md](https://github.com/pointblank-club/syshardn/blob/main/CONTRIBUTING.md)
- [IRIS CONTRIBUTING.md](https://github.com/pointblank-club/IRIS/blob/main/CONTRIBUTING.md)
- [edgeFlow CONTRIBUTING.md](https://github.com/pointblank-club/edgeFlow/blob/main/CONTRIBUTING.md)

Always check the repository-specific documentation for project-specific setup, testing, and contribution requirements.

## Community and Support

- Use **GitHub Issues** for bugs and feature requests
- Use **GitHub Discussions** (where available) for ideas and questions
- Participate in code reviews and help others

## Growth and Ownership

Consistent, high-quality contributors may take on larger roles including:
- Reviewing pull requests
- Guiding technical decisions
- Mentoring new contributors
- Shaping project roadmaps

We value initiative, collaboration, and long-term commitment.

## License

By contributing to any pointblank-club project, you agree that your contributions will be licensed under the terms specified in each repository's LICENSE file.

---

Thank you for contributing to pointblank-club projects. Your time and effort help improve our tools and grow our community.
