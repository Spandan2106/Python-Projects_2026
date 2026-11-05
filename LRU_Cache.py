from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def display(self):
        print("Cache:", dict(self.cache))


# Main class
cache = LRUCache(3)

while True:

    print("\n1. Insert")
    print("2. Get")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")

        cache.put(key, value)

    elif choice == "2":
        key = input("Enter key: ")
        print("Value:", cache.get(key))

    elif choice == "3":
        cache.display()

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
