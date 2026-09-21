# Fixture Lab

This folder introduces `pytest` fixtures, a core testing pattern that lets you create reusable setup for each test without repeating boilerplate code.

The exercises here focus on a simple `BankAccount` model:

- creating a starting balance with a fixture;
- testing deposits and withdrawals; and
- verifying that invalid operations raise `ValueError` when needed.

## What the fixture does

The `account` fixture creates a fresh `BankAccount(100)` for each test, so every test gets a clean starting balance.

```python
@pytest.fixture
def account():
    return BankAccount(100)
```

This keeps the tests focused on behavior instead of repeating setup code in each function.

## Example checks

- `test_deposit`: confirms that a valid deposit increases the balance.
- `test_withdraw`: confirms that a valid withdrawal decreases the balance.

These tests show how fixtures help keep code short, readable, and consistent across multiple test cases.
