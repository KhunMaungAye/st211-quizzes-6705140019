# Bank Exercises

This folder contains two ST211 practice exercises: a simple bank account class and a score-to-letter-grade function. The implementations are in [`bank.py`](bank.py) and [`grade.py`), with tests beside them.

## Bank Account

`BankAccount` stores a balance and provides two operations:

```python
from bank import BankAccount

account = BankAccount(100)
account.deposit(50)  # 150
account.withdraw(30) # 120
```

### Rules

- A new account defaults to a balance of `0`.
- `deposit(amount)` increases the balance and returns the new balance.
- Deposits must be greater than zero. A zero or negative deposit raises `ValueError`.
- `withdraw(amount)` decreases the balance and returns the new balance.
- A withdrawal larger than the current balance raises `ValueError` with an insufficient-funds message.

## Letter Grades

`letter_grade(score)` converts a numeric score into a letter grade:

|  Score | Grade |
| -----: | :---- |
| 80–100 | A     |
|  70–79 | B     |
|  60–69 | C     |
|   0–59 | F     |

Scores outside the range 0 through 100 raise `ValueError`.

```python
from grade import letter_grade

letter_grade(85) # "A"
letter_grade(72) # "B"
letter_grade(60) # "C"
letter_grade(59) # "F"
```

## What These Exercises Practice

These small problems focus on class design, object state, conditional logic, boundary values, and error handling. The tests are especially important at the boundaries: `80`, `79`, `60`, `59`, `0`, and `100` for grades, plus successful and unsuccessful account transactions.

## Running the Tests

From this folder, run:

```bash
python3 -m pytest
```

To run a specific set of tests:

```bash
python3 -m pytest test_bank.py
python3 -m pytest test_grade.py
```
