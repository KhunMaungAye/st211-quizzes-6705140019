# Param Lab: Pytest Parameterization & Data-Driven Testing
---

## Overview

This repository demonstrates how to write clean, maintainable, and DRY (Don't Repeat Yourself) unit tests using pytest. Instead of duplicating test functions for different inputs, this lab covers:

- **Parameterization via `@pytest.mark.parametrize`** (single, multi-variable, and Cartesian products).
- **Custom IDs & Marks** with `pytest.param` to produce readable test logs and handle known bugs.
- **Parametrized Fixtures** with `@pytest.fixture(params=...)` and setup/teardown mechanics.
- **Data-Driven Testing (DDT)** reading external data dynamically from **JSON** and **CSV** files.
- **Exception Testing** with `pytest.raises` applied across multiple invalid input parameters.

---

## Source Modules (Code Under Test)

### 1. `mathutils.py`
Contains elementary utility functions:
- `is_even(n)`: Returns `True` if `n % 2 == 0`, otherwise `False`.
- `factorial(n)`: Computes the factorial of a non-negative integer iteratively; raises `ValueError("Negative Not Allowed")` if $n < 0$.

### 2. `discount.py`
Contains pricing logic:
- `apply_discount(price, percent)`: Calculates discounted price $price \times (1 - \frac{percent}{100})$. Validates that `percent` is within `[0, 100]`, raising `ValueError("Percent must be 0-100")` otherwise.

### 3. `validate.py`
Contains authentication validation helper:
- `is_valid_login(usename, password)`: Returns `True` only if both `username` and `password` are non-empty strings (evaluated via `bool()`).

---

## How Each Test is Done

### 1. `test_param.py` — Single-Argument Parameterization
- **Concept**: The simplest form of `@pytest.mark.parametrize`.
- **How it works**: Passes a single parameter name `"number"` and a list of integer inputs. Pytest generates a distinct subtest for each entry in the list.
- **Test Functions**:
  - `test_even_numbers(number)`: Verifies `[2, 4, 6, 8, 100]` return `True`.
  - `test_odd_numbers(number)`: Verifies `[1, 3, 5, 7, 99]` return `False`.
- **Generated Test Count**: 10 tests (5 even + 5 odd).

```python
@pytest.mark.parametrize("number", [2, 4, 6, 8, 100])
def test_even_numbers(number):
    assert is_even(number) is True
```

---

### 2. `test_factorial.py` — Multi-Argument Parameterization
- **Concept**: Testing input-output pairs together.
- **How it works**: Passes comma-separated parameter names `"n,expected"` and a list of 2-element tuples `[(0, 1), (1, 1), (2, 2), ...]`. Each tuple is unpacked directly into the test arguments `(n, expected)`.
- **Test Function**: `test_factorial(n, expected)` verifies `factorial(n) == expected`.
- **Generated Test Count**: 6 tests.

```python
@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_factorial(n, expected):
    assert factorial(n) == expected
```

---

### 3. `test_discount.py` — Business Logic Verification
- **Concept**: Testing formulas with 3 or more arguments `(price, percent, expected)`.
- **How it works**: Tests edge cases and typical percentages (0% no discount, 50% half off, 100% free, 25%, 10%).
- **Test Function**: `test_discount_calculations(price, percent, expected)` asserts that `apply_discount(price, percent) == expected`.
- **Generated Test Count**: 5 tests.

```python
@pytest.mark.parametrize("price, percent, expected", [
    (100, 0, 100),
    (100, 50, 50),
    (100, 100, 0),
    (200, 25, 150),
    (80, 10, 72),
])
def test_discount_calculations(price, percent, expected):
    assert apply_discount(price, percent) == expected
```

---

### 4. `test_discount_errors.py` — Parameterized Exception Testing
- **Concept**: Combining `@pytest.mark.parametrize` with `pytest.raises(...)` to verify error boundaries.
- **How it works**: Supplies invalid values (`-1`, `-50`, `101`, `200`) to `bad_percent`. Inside the test, a `with pytest.raises(ValueError):` context manager confirms that the function correctly rejects all inputs outside the range `[0, 100]`.
- **Test Function**: `test_invalid_percent_raises(bad_percent)`.
- **Generated Test Count**: 4 tests.

```python
@pytest.mark.parametrize("bad_percent", [-1, -50, 101, 200])
def test_invalid_percent_raises(bad_percent):
    with pytest.raises(ValueError):
        apply_discount(100, bad_percent)
```

---

### 5. `test_default_ids.py` — Default Pytest ID Generation
- **Concept**: Observing how pytest names test cases when no custom ID is provided.
- **How it works**: Parameterizes a complex object (dictionaries `{"name": "Alice", "age": 30}`). Because dictionaries are mutable and non-scalar, pytest generates fallback identifiers in the test runner output: `user0`, `user1`.
- **Test Function**: `test_user_has_name(user)`.
- **Generated Test Count**: 2 tests (`test_user_has_name[user0]`, `test_user_has_name[user1]`).

```python
@pytest.mark.parametrize("user", [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
])
def test_user_has_name(user):
    assert "name" in user
```

---

### 6. `test_param_ids.py` — Custom Test IDs
- **Concept**: Giving clear, semantic names to test cases using `pytest.param(..., id=...)`.
- **How it works**: Instead of seeing raw values `[100-0-100]` in the console, `pytest.param(..., id="no_discount")` displays `test_discount[no_discount]`. This makes test logs instantly understandable during CI/CD failures.
- **Test Function**: `test_discount(price, percent, expected)`.
- **Generated Test Count**: 1 test.

```python
@pytest.mark.parametrize("price, percent, expected", [
    pytest.param(100, 0, 100, id="no_discount"),
])
def test_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected
```

---

### 7. `test_param_marks.py` — Applying Marks (`xfail`) to Specific Cases
- **Concept**: Tagging specific parameter cases without marking the entire test function.
- **How it works**: Uses `pytest.param(..., marks=pytest.mark.xfail)` on individual test rows.
  - `(2, 4)` and `(3, 9)` pass normally.
  - `(5, 20)` represents a known bug or intentional failure ($5^2 \neq 20$). Pytest marks this row as `XFAIL` (Expected Failure) without failing the whole test suite.
- **Test Function**: `test_square(value, expected)`.
- **Generated Test Count**: 3 tests (2 PASSED, 1 XFAIL).

```python
@pytest.mark.parametrize("value, expected", [
    pytest.param(2, 4, id="two_squared"),
    pytest.param(3, 9, id="three_squared"),
    pytest.param(5, 20, id="known_bug", marks=pytest.mark.xfail)
])
def test_square(value, expected):
    assert value ** 2 == expected
```

---

### 8. `test_multi.py` — Cartesian Product / Stacked Decorators
- **Concept**: Combining multiple parameter sets to generate all possible combinations.
- **How it works**: Stacking multiple `@pytest.mark.parametrize` decorators produces the Cartesian product of the inputs.
  - Decorator 1: `x` has 3 values (`[1, 2, 3]`).
  - Decorator 2: `y` has 2 values (`[10, 20]`).
  - Result: $3 \times 2 = 6$ test executions: `(10, 1)`, `(10, 2)`, `(10, 3)`, `(20, 1)`, `(20, 2)`, `(20, 3)`.
- **Test Function**: `test_combinations(x, y)` asserts `x + y > 0`.
- **Generated Test Count**: 6 tests.

```python
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_combinations(x, y):
    assert x + y > 0
    print(f"\n Testing x = {x}, y= {y}")
```

---

### 9. `test_parm_fixture.py` — Parametrized Fixtures
- **Concept**: Parametrizing at the fixture level so any test that requests the fixture runs across all configurations.
- **How it works**: `@pytest.fixture(params=["sqlite", "postgres", "mysql"])` defines a fixture with `request.param`. When `test_database_connection` requests `database_type`, pytest automatically runs the test 3 times, once for each database backend.
- **Test Function**: `test_database_connection(database_type)`.
- **Generated Test Count**: 3 tests.

```python
@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def database_type(request):
    return request.param

def test_database_connection(database_type):
    print(f"\n Testing with {database_type}")
    assert database_type in ["sqlite", "postgres", "mysql"]
```

---

### 10. `test_browsers.py` — Fixture Setup and Teardown (`yield`)
- **Concept**: Cross-browser / environment testing with lifecycle management.
- **How it works**: The `browser` fixture is parameterized over `["chrome", "firefox", "safari"]`. Using Python's `yield`:
  - Everything before `yield` runs as **Setup** (e.g. launching browser).
  - The test runs.
  - Everything after `yield` runs as **Teardown** (e.g. closing browser).
- Because two test functions (`test_page_loads` and `test_button_clickable`) both request `browser`, each test runs for all 3 browsers ($2 \times 3 = 6$ executions).
- **Generated Test Count**: 6 tests.

```python
@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request):
    browser_name = request.param
    print(f"\n [setup]  launching {browser_name}")
    yield browser_name
    print(f"    [teardown] closing {browser_name}")

def test_page_loads(browser):
    assert browser is not None

def test_button_clickable(browser):
    assert len(browser) > 0
```

---

### 11. `test_data_driven.py` — External JSON Data Source
- **Concept**: Decoupling test data from test logic using JSON files.
- **How it works**:
  - `load_cases()` opens `test_cases.json`, parses JSON objects, and returns a list of tuples `[(case["input"], case["expected"]), ...]`.
  - The function is called directly inside `@pytest.mark.parametrize("text, expected", load_cases())`.
- **Test Function**: `test_uppercase(text, expected)` verifies `text.upper() == expected`.
- **Generated Test Count**: 4 tests.

```python
def load_cases():
    with open("test_cases.json") as f:
        data = json.load(f)
    return [(case["input"], case["expected"]) for case in data]

@pytest.mark.parametrize("text, expected", load_cases())
def test_uppercase(text, expected):
    assert text.upper() == expected
```

---

### 12. `test_csv_driven.py` — External CSV Data Source
- **Concept**: Driving tests using standard CSV spreadsheets.
- **How it works**:
  - `load_login_cases()` uses `csv.DictReader` to parse `logins.csv`.
  - Converts string `"True"` into a real boolean: `row["valid"] == "True"`.
  - Returns `[(username, password, expected_validity), ...]`.
  - Passes rows to `test_login_validation(username, password, expected)`.
- Covers valid users (`admin`, `user`), missing passwords (`hacker,`), and missing usernames (`,nopassword`).
- **Generated Test Count**: 4 tests.

```python
def load_login_cases():
    cases = []
    with open("logins.csv") as f:
        for row in csv.DictReader(f):
            expected = row["valid"] == "True"
            cases.append((row["username"], row["password"], expected))
    return cases

@pytest.mark.parametrize("username, password, expected", load_login_cases())
def test_login_validation(username, password, expected):
    assert is_valid_login(username, password) == expected
```

---

## Quick Reference Table
---

| Test File | Tested Module | Pytest Feature / Concept | Data Source | Test Cases Generated |
| :--- | :--- | :--- | :--- | :---: |
| `test_param.py` | `mathutils.py` | Single-parameter `@pytest.mark.parametrize` | In-code list | 10 |
| `test_factorial.py` | `mathutils.py` | Multi-parameter tuple unpacking | In-code list of tuples | 6 |
| `test_discount.py` | `discount.py` | Multi-argument calculation testing | In-code list of tuples | 5 |
| `test_discount_errors.py` | `discount.py` | Parameterized `pytest.raises` for exceptions | In-code list | 4 |
| `test_default_ids.py` | *None (Self)* | Default fallback ID generation for dicts | In-code list of dicts | 2 |
| `test_param_ids.py` | `discount.py` | Custom human-readable IDs with `pytest.param(..., id=...)` | In-code `pytest.param` | 1 |
| `test_param_marks.py` | *None (Self)* | Per-row test marks with `pytest.param(..., marks=xfail)` | In-code `pytest.param` | 3 |
| `test_multi.py` | *None (Self)* | Cartesian product via stacked decorators | Two in-code lists | 6 |
| `test_parm_fixture.py` | *None (Self)* | Parametrized fixtures (`request.param`) | Fixture `params=[...]` | 3 |
| `test_browsers.py` | *None (Self)* | Parametrized fixture setup/teardown (`yield`) | Fixture `params=[...]` | 6 |
| `test_data_driven.py` | *Built-in `str.upper`* | Dynamic data-driven testing via JSON file | `test_cases.json` | 4 |
| `test_csv_driven.py` | `validate.py` | Dynamic data-driven testing via CSV file | `logins.csv` | 4 |
| **Total** | | | | **54 tests** (53 passed, 1 xfailed) |

---

## How to Run the Tests

### 1. Run the entire test suite
```bash
pytest -v
```

### 2. Run with standard output printed (setup/teardown prints)
```bash
pytest -v -s
```

### 3. Run a specific test file
```bash
# Run only CSV data-driven tests
pytest -v test_csv_driven.py

# Run only fixture lifecycle tests
pytest -v -s test_browsers.py
