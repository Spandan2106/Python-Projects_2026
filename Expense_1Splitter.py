class ExpenseSplitter:

    def __init__(self):
        self.balances = {}

    def add_person(self, name):
        self.balances.setdefault(name, 0)

    def add_expense(self, paid_by, amount, participants):

        if amount <= 0 or not participants:
            print("Invalid expense!")
            return

        if paid_by not in self.balances:
            print("Payer not found!")
            return

        if any(p not in self.balances for p in participants):
            print("Participant not found!")
            return

        share = amount / len(participants)

        self.balances[paid_by] += amount

        for person in participants:
            self.balances[person] -= share

        print("Expense added!")

    def show_balances(self):
        for person, balance in self.balances.items():
            print(person, ":", round(balance, 2))

    def settle(self):

        creditors = []
        debtors = []

        for person, balance in self.balances.items():
            if balance > 0.001:
                creditors.append([person, balance])
            elif balance < -0.001:
                debtors.append([person, -balance])

        i = 0
        j = 0

        print("\nSuggested Settlements:")

        while i < len(debtors) and j < len(creditors):

            amount = min(debtors[i][1], creditors[j][1])

            print(debtors[i][0], "pays",
                  creditors[j][0], round(amount, 2))

            debtors[i][1] -= amount
            creditors[j][1] -= amount

            if debtors[i][1] < 0.001:
                i += 1

            if creditors[j][1] < 0.001:
                j += 1


splitter = ExpenseSplitter()

while True:
    print("\n1. Add Person")
    print("2. Add Expense")
    print("3. Show Balances")
    print("4. Settle Expenses")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        splitter.add_person(input("Name: "))

    elif choice == "2":
        payer = input("Paid by: ")
        amount = float(input("Amount: "))
        participants = input(
            "Participants (comma separated): "
        ).split(",")

        participants = [p.strip() for p in participants]

        splitter.add_expense(payer, amount, participants)

    elif choice == "3":
        splitter.show_balances()

    elif choice == "4":
        splitter.settle()

    elif choice == "5":
        break
