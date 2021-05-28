class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        self._balance -= amount
        print("Operation successful")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance can not lower 0")
        self._balance = amount


bank_account1 = BankAccount(100)
print(bank_account1.balance)
bank_account1.balance = 55555
print(bank_account1.balance)
