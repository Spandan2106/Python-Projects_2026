class Wallet:

    def __init__(self, user):
        self.user = user
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        self.balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn {amount}")

    def display(self):
        print(self.user, "Balance:", self.balance)


class WalletSystem:

    def __init__(self):
        self.wallets = {}

    def create_wallet(self, user):
        if user in self.wallets:
            print("Wallet already exists!")
            return

        self.wallets[user] = Wallet(user)
        print("Wallet created!")

    def transfer(self, sender, receiver, amount):

        if sender not in self.wallets or receiver not in self.wallets:
            print("Wallet not found!")
            return

        if sender == receiver or amount <= 0:
            print("Invalid transfer!")
            return

        source = self.wallets[sender]
        destination = self.wallets[receiver]

        if source.balance < amount:
            print("Insufficient balance!")
            return

        source.balance -= amount
        destination.balance += amount

        source.history.append(f"Sent {amount} to {receiver}")
        destination.history.append(f"Received {amount} from {sender}")

        print("Transfer successful!")


system = WalletSystem()

while True:
    print("\n1. Create Wallet")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.create_wallet(input("Username: "))

    elif choice in ["2", "3"]:
        user = input("Username: ")

        if user not in system.wallets:
            print("Wallet not found!")
            continue

        amount = float(input("Amount: "))

        if choice == "2":
            system.wallets[user].deposit(amount)
        else:
            system.wallets[user].withdraw(amount)

    elif choice == "4":
        sender = input("Sender: ")
        receiver = input("Receiver: ")
        amount = float(input("Amount: "))
        system.transfer(sender, receiver, amount)

    elif choice == "5":
        user = input("Username: ")

        if user in system.wallets:
            system.wallets[user].display()
        else:
            print("Wallet not found!")

    elif choice == "6":
        user = input("Username: ")

        if user in system.wallets:
            for transaction in system.wallets[user].history:
                print(transaction)
        else:
            print("Wallet not found!")

    elif choice == "7":
        break
