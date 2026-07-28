# Leetcode

Python solutions and tests for Leetcode problems.

## Repository Layout

Each problem lives in its own numbered directory:

```text
0001_two_sum/
  README.md
  solution.py
  test_solution.py
```

## Setup

This repo uses `uv` for Python dependency management.

```bash
make install
```

## Common Commands

```bash
make test   # run the pytest suite
make lint   # run prek / Ruff hooks
make check  # run tests and linting
```

## Adding A Problem

1. Create a numbered directory, for example `0002_add_two_numbers/`.
2. Add the problem notes to `README.md`.
3. Add the implementation to `solution.py`.
4. Add pytest coverage in `test_solution.py`.
5. Run `make check` before opening a pull request.

## Tooling

- `pytest` runs the test suite.
- `prek` runs pre-commit hooks.
- Ruff checks and formats Python code through `.pre-commit-config.yaml`.
- GitHub Actions runs tests on pull requests and pushes to `main`.
