class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        self.__account_balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

