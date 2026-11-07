class Product:

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(self.product_id, self.name,
              self.price, self.quantity)


class Inventory:

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product already exists!")
            return

        self.products[product.product_id] = product
        print("Product added!")

    def update_stock(self, product_id, quantity):
        if product_id not in self.products:
            print("Product not found!")
            return

        if self.products[product_id].quantity + quantity < 0:
            print("Insufficient stock!")
            return

        self.products[product_id].quantity += quantity
        print("Stock updated!")

    def search_product(self, product_id):
        product = self.products.get(product_id)

        if product:
            product.display()
        else:
            print("Product not found!")

    def display_inventory(self):
        for product in self.products.values():
            product.display()

    def total_value(self):
        total = sum(
            p.price * p.quantity
            for p in self.products.values()
        )
        print("Total Inventory Value:", total)


inventory = Inventory()

while True:
    print("\n1. Add Product")
    print("2. Update Stock")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Total Inventory Value")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pid = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        if price < 0 or quantity < 0:
            print("Invalid values!")
        else:
            inventory.add_product(
                Product(pid, name, price, quantity)
            )

    elif choice == "2":
        pid = input("Product ID: ")
        quantity = int(input("Stock change (+/-): "))
        inventory.update_stock(pid, quantity)

    elif choice == "3":
        inventory.search_product(input("Product ID: "))

    elif choice == "4":
        inventory.display_inventory()

    elif choice == "5":
        inventory.total_value()

    elif choice == "6":
        break
