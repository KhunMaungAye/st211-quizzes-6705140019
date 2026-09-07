from bank import BankAccount

def test_deposit():
    account = BankAccount(100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_withdraw():
    account = BankAccount(100)
    new_balance = account.withdraw(30)
    assert new_balance == 70
