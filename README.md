# ST211 Quizzes and Exercises

This repository contains quizzes, programming exercises, and practice tests for the ST211 class. Each exercise is kept in its own folder so that the implementation, tests, and explanation stay together.

## Repository Structure

```text
st211-quizzes-6705140019/
├── Roman/
│   ├── roman.py
│   ├── test_roman.py
│   └── README.md
├── Bank/
│   ├── bank.py
│   ├── grade.py
│   ├── test_bank.py
│   ├── test_dependent.py
│   ├── test_grade.py
│   └── README.md
├── assert-lab/
│   ├── shopping.py
│   ├── test_collections.py
│   ├── test_floats.py
│   ├── test_shopping.py
│   └── README.md
└── validate/
    ├── validators.py
    ├── test_positive.py
    ├── test_negative.py
    └── README.md
```

## Exercises

### Roman

The Roman exercise converts Roman numerals to integers and integers to Roman numerals. It demonstrates dictionaries, iteration, validation, and the rules for subtractive notation. See [Roman/README.md](Roman/README.md).

### Bank

The Bank exercise contains two small independent problems:

- `BankAccount`, which supports deposits and withdrawals while tracking a balance.
- `letter_grade`, which converts a score from 0 to 100 into a letter grade.

See [Bank/README.md](Bank/README.md) for the rules and examples.

### Assert Lab

The assert-lab exercise introduces assertion-based test patterns for a small `ShoppingCart`, collection comparison checks, and float comparisons using `pytest.approx()`. See [assert-lab/README.md](assert-lab/README.md).

### Validate

The validate exercise provides a small validation helper suite that checks valid email and age inputs and rejects invalid forms, out-of-range ages, and non-integer age types. See [validate/README.md](validate/README.md).

## Running the Tests

Install `pytest` if it is not already available:

```bash
python3 -m pip install pytest
```

Run all tests from the repository root:

```bash
python3 -m pytest
```

Run one exercise independently:

```bash
python3 -m pytest Roman
python3 -m pytest Bank
```

## Learning Goals

These exercises provide practice with:

- writing small, reusable Python functions and classes;
- applying input rules and raising useful `ValueError` exceptions;
- translating requirements into automated tests;
- checking boundary cases and invalid input; and
- using `pytest` to verify program behavior.

Each new class quiz or exercise can follow the same pattern: place the implementation and tests in the appropriate folder, document the rules, and run the tests before submitting.
