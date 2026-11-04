#python class to deposit or withdraw amount from bank account and display the balance ,class "Account" with methods deposit , withdraw and display balance.
class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")
# Example usage
account = Account()
while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.display_balance()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        