# Should System Guide

## Project Overview

**Should** is a lightweight assertion framework designed for **MicroPython** and **MicroPytest**.
It offers a fluent, chainable API that allows for writing expressive and readable tests.
The project aims to provide a simple and effective way to handle assertions in a **MicroPython** environment.


## Tech stack

- **Programming language**: **MicroPython** 1.28

- **Testing**: **unittest**

- **Dependency management**:
  [Poetry](https://python-poetry.org) is used for managing project dependencies and virtual environments.

- **Linting and formatting**: The project uses [Ruff](https://docs.astral.sh/ruff) for both high-performance linting and code formatting.
  [Pyright](https://github.com/microsoft/pyright) is also used for static type checking.


## Project structure

```
/
├───.github/              # GitHub Actions workflows and templates
├───scripts/
│   ├───install.sh        # Dependency installation script
│   └───tests.sh          # Test execution script
├───should/
│   ├───__init__.py
│   └───_should.py        # Core assertion logic
├───tests/
│   └───unit/
│       └───should_test.py # Unit tests
├───pyproject.toml        # Project metadata and dependencies (Poetry)
├───README.md             # Project overview
└───...
```

- **`should/_should.py`**:
  This is the main file containing the core logic of the assertion library.
  It includes the ***`AssertValue`*** class, which provides all the assertion methods and the ***`AssertThrowContext`*** for exception testing.

- **`tests/unit/should_test.py`**:
  Contains the unit tests for the **Should** library, ensuring its correctness.

- **`scripts/`**:
  Contains shell scripts for common development tasks like running tests.


## Development workflow and commands

All commands should be run from the project root:

- **Running Tests**.
  The primary test script executes unit tests using a **MicroPython** environment:

  ```bash
  poetry run scripts/tests.sh
  ```

- **Linting**.
  Check the codebase for style issues and errors with **Ruff** and **Pyright**:

  ```bash
  poetry run pyright
  poetry run ruff check
  ```

- **Formatting**:
  Automatically format the code using **Ruff**:

  ```bash
  poetry run ruff format .
  ```
