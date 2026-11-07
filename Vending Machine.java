class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class VendingMachine:

    def __init__(self):
        self.products = {
            "A1": Product("Chips", 20, 5),
            "A2": Product("Juice", 30, 5),
            "A3": Product("Chocolate", 40, 3)
        }

        self.balance = 0

    def display_products(self):
        for code, product in self.products.items():
            print(code, product.name,
                  product.price, product.quantity)

    def insert_money(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        self.balance += amount
        print("Current balance:", self.balance)

    def purchase(self, code):
        product = self.products.get(code)

        if product is None:
            print("Invalid product!")
            return

        if product.quantity == 0:
            print("Out of stock!")
            return

        if self.balance < product.price:
            print("Insufficient money!")
            return

        self.balance -= product.price
        product.quantity -= 1

        print("Dispensing:", product.name)
        print("Change:", self.balance)

        self.balance = 0

    def refund(self):
        print("Refund:", self.balance)
        self.balance = 0


machine = VendingMachine()

while True:
    print("\n1. Display Products")
    print("2. Insert Money")
    print("3. Purchase")
    print("4. Refund")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        machine.display_products()

    elif choice == "2":
        amount = int(input("Enter amount: "))
        machine.insert_money(amount)

    elif choice == "3":
        code = input("Product Code: ")
        machine.purchase(code)

    elif choice == "4":
        machine.refund()

    elif choice == "5":
        machine.refund()
        break
