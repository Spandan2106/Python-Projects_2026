class Database:

    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value
        print("Data saved!")

    def get(self, key):
        if key in self.data:
            print("Value:", self.data[key])
        else:
            print("Key not found!")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            print("Record deleted!")
        else:
            print("Key not found!")

    def display(self):
        print(self.data)


db = Database()

while True:
    print("\n1. Insert")
    print("2. Retrieve")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        db.set(key, value)

    elif choice == "2":
        key = input("Enter key: ")
        db.get(key)

    elif choice == "3":
        key = input("Enter key: ")
        db.delete(key)

    elif choice == "4":
        db.display()

    elif choice == "5":
        break
