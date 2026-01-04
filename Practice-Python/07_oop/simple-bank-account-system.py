
import shutil

width = shutil.get_terminal_size().columns
print("=" * width)
print("BANK ACCOUNT SYSTEM".center(width))
print("=" * width)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"Balance: {self.balance}")


name = input("Enter your name: ")
balance = float(input("Enter your initial balance: "))

account = BankAccount(name, balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

account.show_balance()
