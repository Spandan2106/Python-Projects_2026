class FoodOrder:

    def __init__(self):
        self.menu = {
            "Burger": 100,
            "Pizza": 250,
            "Pasta": 180,
            "Sandwich": 80
        }

        self.cart = {}
        self.status = "Not Ordered"

    def display_menu(self):
        for item, price in self.menu.items():
            print(item, ":", price)

    def add_item(self, item, quantity):
        if item not in self.menu:
            print("Item unavailable!")
        elif quantity <= 0:
            print("Invalid quantity!")
        else:
            self.cart[item] = self.cart.get(item, 0) + quantity
            print("Item added!")

    def calculate_bill(self):
        total = 0

        for item, quantity in self.cart.items():
            total += self.menu[item] * quantity

        return total

    def place_order(self):
        if not self.cart:
            print("Cart is empty!")
            return

        print("Order placed!")
        print("Total Bill:", self.calculate_bill())
        self.status = "Preparing"

    def track_order(self):
        print("Order Status:", self.status)

    def update_status(self, status):
        self.status = status
        print("Status updated!")


order = FoodOrder()

while True:
    print("\n1. Display Menu")
    print("2. Add Item")
    print("3. View Bill")
    print("4. Place Order")
    print("5. Track Order")
    print("6. Update Status")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        order.display_menu()

    elif choice == "2":
        item = input("Enter item: ")
        quantity = int(input("Quantity: "))
        order.add_item(item, quantity)

    elif choice == "3":
        print("Total:", order.calculate_bill())

    elif choice == "4":
        order.place_order()

    elif choice == "5":
        order.track_order()

    elif choice == "6":
        status = input("Enter new status: ")
        order.update_status(status)

    elif choice == "7":
        break
