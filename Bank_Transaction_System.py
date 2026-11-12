class BankAccount:

    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        self.balance += amount
        self.history.append("Deposited: " + str(amount))
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.history.append("Withdrawn: " + str(amount))
            print("Withdrawal successful!")

    def display(self):
        print("Account:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)

    def show_history(self):
        for transaction in self.history:
            print(transaction)


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_no, name, balance):
        if account_no in self.accounts:
            print("Account already exists!")
        elif balance < 0:
            print("Invalid balance!")
        else:
            self.accounts[account_no] = BankAccount(
                account_no, name, balance
            )
            print("Account created!")

    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            print("Account not found!")
            return

        if amount <= 0:
            print("Invalid amount!")
            return

        a = self.accounts[sender]
        b = self.accounts[receiver]

        if a.balance >= amount:
            a.balance -= amount
            b.balance += amount
            a.history.append("Transferred: " + str(amount))
            b.history.append("Received: " + str(amount))
            print("Transfer successful!")
        else:
            print("Insufficient balance!")


bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc = input("Account number: ")
        name = input("Name: ")
        amount = float(input("Initial balance: "))
        bank.create_account(acc, name, amount)

    elif choice in ["2", "3"]:
        acc = input("Account number: ")

        if acc not in bank.accounts:
            print("Account not found!")
            continue

        amount = float(input("Amount: "))

        if choice == "2":
            bank.accounts[acc].deposit(amount)
        else:
            bank.accounts[acc].withdraw(amount)

    elif choice == "4":
        sender = input("Sender account: ")
        receiver = input("Receiver account: ")
        amount = float(input("Amount: "))
        bank.transfer(sender, receiver, amount)

    elif choice == "5":
        acc = input("Account number: ")

        if acc in bank.accounts:
            bank.accounts[acc].display()
        else:
            print("Account not found!")

    elif choice == "6":
        acc = input("Account number: ")

        if acc in bank.accounts:
            bank.accounts[acc].show_history()
        else:
            print("Account not found!")

    elif choice == "7":
        break
