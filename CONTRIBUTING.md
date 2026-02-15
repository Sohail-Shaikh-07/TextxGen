# Contributing to TextxGen

Thank you for your interest in contributing to TextxGen.

## Scope of Contributions

You can contribute by:
- Fixing bugs
- Improving documentation
- Adding tests
- Adding or refining endpoint features
- Improving examples and developer experience

## Development Setup

1. Fork the repository and clone your fork.
2. Create and activate a virtual environment.
3. Install dependencies.

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Project Structure

- `textxgen/`: core package code
- `textxgen/endpoints/`: endpoint implementations
- `textxgen/tests/`: unit tests
- `textxgen/examples/`: usage examples

## Branch and Commit Guidelines

1. Create a feature branch from `main`:
```bash
git checkout -b feat/short-description
```
2. Keep commits focused and readable.
3. Use clear commit messages, for example:
- `fix: handle invalid payload in chat endpoint`
- `docs: improve completion examples`

## Code Style Guidelines

- Target Python 3.8+ compatibility.
- Keep functions small and focused.
- Reuse existing exception types from `textxgen/exceptions.py`.
- Preserve backward-compatible public APIs unless discussed in the PR.

## Testing

Run tests before opening a PR:

```bash
python -m unittest discover -s textxgen/tests -p "test_*.py"
```

When adding a new feature or bug fix:
- Add or update tests in `textxgen/tests/`.
- Cover both success and failure paths when relevant.

## Pre-PR Checklist

Before opening a PR, verify:

- [ ] Branch is up to date with `main`
- [ ] Code is scoped to one logical change
- [ ] New/changed behavior is covered by tests
- [ ] All tests pass locally
- [ ] Public API changes are documented in `README.md` (if applicable)
- [ ] Examples are updated when behavior changes
- [ ] Commit history is clean and understandable

## Pull Request Guidance

Please include the following in your PR description:

1. What changed
2. Why it changed
3. How to validate it
4. Any breaking changes (if any)

A helpful PR template:

```md
## Summary
- 

## Motivation
- 

## Validation
- [ ] `python -m unittest discover -s textxgen/tests -p "test_*.py"`

## Breaking Changes
- None / Describe here
```

## Reporting Issues

When opening an issue, include:
- Expected behavior
- Actual behavior
- Steps to reproduce
- Python version and OS
- Minimal code sample (if possible)

## Communication

Be respectful and constructive in discussions and reviews. Clear, actionable feedback helps everyone move faster.
