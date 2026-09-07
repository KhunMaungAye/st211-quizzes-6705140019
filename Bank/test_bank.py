from bank import BankAccount

def test_deposit_increase_balance():
    account = BankAccount(100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_withdraw_decrease_balance():
    account = BankAccount(1000)
    new_balance = account.withdraw(200)
    assert new_balance == 800
