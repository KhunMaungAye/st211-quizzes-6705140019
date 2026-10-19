# Mocking Exercise

A Python class exercise demonstrating **Unit Testing**, **Mocking Non-Deterministic Functions**, and **Parameterized Boundary Value Testing** 

---

## Overview

In software development, functions often depend on random numbers, current time, network APIs, or database queries. Because these dependencies produce non-deterministic (variable) outputs, standard assertions can be flaky or impossible to verify consistently.

This exercise demonstrates:
1. **Testing Non-Deterministic Logic**: Verifying that a random generator stays within defined bounds.
2. **Mocking with `patch`**: Overriding dependencies in tests so functions can be tested in deterministic isolation.
3. **Boundary Value Testing**: Ensuring conditional boundaries (`< 0`, `< 15`, `< 25`, `>= 25`) behave correctly at their exact edge values.
4. **Parameterized Testing**: Running clean, DRY (Don't Repeat Yourself) table-driven tests using `@pytest.mark.parametrize`.

---

## Project Structure

```text
.
├── weather.py         # Business logic: temperature generation and weather description
├── test_weather.py    # Test suite: unit tests, mocking, and boundary tests
└── README.md          # Project documentation and study guide
```

---

## Code Walkthrough

### 1. `weather.py` (Source Code)

- **`get_temperature()`**: Returns a random integer between `-10` and `40` (°C) using Python's `random.randint`.
- **`describe_weather()`**: Calls `get_temperature()` and classifies the temperature:

| Temperature Range | Condition | Output |
| :--- | :--- | :--- |
| `temp < 0` | Below freezing | `"Freezing"` |
| `0 <= temp < 15` | Cold | `"Cold"` |
| `15 <= temp < 25` | Moderate / Mild | `"Pleasant"` |
| `temp >= 25` | Warm to hot | `"Hot"` |

### 2. `test_weather.py` (Test Suite)

- **Range Assertion**:
  ```python
  def test_get_temperature_range():
      temp = get_temperature()
      assert -10 <= temp <= 40
  ```
  Validates that `get_temperature()` strictly respects the upper and lower limits.

- **Mocking with Context Manager**:
  ```python
  def test_hot_weather():
      with patch("weather.get_temperature", return_value=30):
          assert describe_weather() == "Hot"
  ```
  `unittest.mock.patch` intercepts calls to `weather.get_temperature` during the `with` block and replaces the call with a constant `30`.

- **Parameterized Boundary Value Tests**:
  ```python
  @pytest.mark.parametrize("temperature, expected", [
      (-10, "Freezing"), # Lower bound
      (-1,  "Freezing"), # Just below 0
      (0,   "Cold"),     # Lower boundary for Cold
      (14,  "Cold"),     # Upper boundary for Cold (< 15)
      (15,  "Pleasant"), # Lower boundary for Pleasant
      (24,  "Pleasant"), # Upper boundary for Pleasant (< 25)
      (25,  "Hot"),      # Lower boundary for Hot
      (40,  "Hot"),      # Maximum possible temperature
  ])
  def test_describe_weather(temperature, expected):
      with patch("weather.get_temperature", return_value=temperature):
          assert describe_weather() == expected
  ```
  Tests every critical boundary on both sides of each transition point to prevent off-by-one errors.

---

## Getting Started

### Prerequisites

- Python 3.8+
- `pytest`

### Installation

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install `pytest`:
   ```bash
   pip install pytest
   ```

### Running Tests

Execute all tests with standard output:
```bash
pytest
```

Run tests in verbose mode to see each parameter case:
```bash
pytest -v
```

Expected output:
```text
test_weather.py::test_get_temperature_range PASSED
test_weather.py::test_hot_weather PASSED
test_weather.py::test_freezing_weather PASSED
test_weather.py::test_describe_weather[-10-Freezing] PASSED
test_weather.py::test_describe_weather[-1-Freezing] PASSED
test_weather.py::test_describe_weather[0-Cold] PASSED
test_weather.py::test_describe_weather[14-Cold] PASSED
test_weather.py::test_describe_weather[15-Pleasant] PASSED
test_weather.py::test_describe_weather[24-Pleasant] PASSED
test_weather.py::test_describe_weather[25-Hot] PASSED
test_weather.py::test_describe_weather[40-Hot] PASSED
```

---

## Key Takeaways 

1. **Where to patch**: Always patch where the object is *looked up* / *used*, not necessarily where it was defined. In `test_weather.py`, we patch `"weather.get_temperature"` because `describe_weather` looks it up in the `weather` module namespace.
2. **Deterministic Tests**: Tests should never rely on randomness or real external services (like APIs or clocks) when verifying business logic.
3. **Boundary Value Analysis**: Most bugs in conditional logic occur at the thresholds (`<` vs `<=`). Testing numbers immediately below, at, and above boundaries catches subtle regressions.

