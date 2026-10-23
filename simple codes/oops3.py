#BankAccount class with deposit and withdraw. by oops
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
# Example usage
account = BankAccount("123456789")
account.display()
account.deposit(500)
account.withdraw(200)
account.withdraw(400)
account.display()