class FileSystem:

    def __init__(self):
        self.root = {"type": "folder", "children": {}}

    def create_folder(self, path):
        self.create_item(path, "folder")

    def create_file(self, path):
        self.create_item(path, "file")

    def create_item(self, path, item_type):

        parts = [p for p in path.split("/") if p]

        if not parts:
            print("Invalid path!")
            return

        current = self.root

        for folder in parts[:-1]:
            if folder not in current["children"]:
                print("Parent folder not found!")
                return

            current = current["children"][folder]

            if current["type"] != "folder":
                print("Parent is not a folder!")
                return

        name = parts[-1]

        if name in current["children"]:
            print("Item already exists!")
            return

        current["children"][name] = {
            "type": item_type,
            "children": {} if item_type == "folder" else None
        }

        print(item_type.capitalize(), "created!")

    def delete_item(self, path):

        parts = [p for p in path.split("/") if p]

        if not parts:
            print("Cannot delete root!")
            return

        current = self.root

        for folder in parts[:-1]:
            if folder not in current["children"]:
                print("Path not found!")
                return

            current = current["children"][folder]

            if current["type"] != "folder":
                print("Invalid path!")
                return

        if parts[-1] not in current["children"]:
            print("Item not found!")
            return

        del current["children"][parts[-1]]
        print("Item deleted!")

    def display(self, node=None, level=0):

        if node is None:
            node = self.root

        for name, item in node["children"].items():

            print("  " * level + name,
                  "[" + item["type"] + "]")

            if item["type"] == "folder":
                self.display(item, level + 1)


fs = FileSystem()

while True:
    print("\n1. Create Folder")
    print("2. Create File")
    print("3. Delete Item")
    print("4. Display File System")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        fs.create_folder(input("Enter path: "))

    elif choice == "2":
        fs.create_file(input("Enter path: "))

    elif choice == "3":
        fs.delete_item(input("Enter path: "))

    elif choice == "4":
        fs.display()

    elif choice == "5":
        break
