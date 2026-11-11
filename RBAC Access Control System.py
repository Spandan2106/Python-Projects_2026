class Role:

    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def grant(self, permission):
        self.permissions.add(permission)


class AccessControl:

    def __init__(self):
        self.roles = {}
        self.users = {}

    def create_role(self, name):

        if name in self.roles:
            print("Role already exists!")
            return

        self.roles[name] = Role(name)

    def grant_permission(self, role, permission):

        if role not in self.roles:
            print("Role not found!")
            return

        self.roles[role].grant(permission)

    def assign_role(self, username, role):

        if role not in self.roles:
            print("Role not found!")
            return

        self.users.setdefault(username, set()).add(role)

    def authorize(self, username, permission):

        for role in self.users.get(username, set()):

            if permission in self.roles[role].permissions:
                return True

        return False


acl = AccessControl()

acl.create_role("admin")
acl.create_role("reader")

acl.grant_permission("admin", "user:create")
acl.grant_permission("admin", "user:delete")
acl.grant_permission("reader", "user:read")

acl.assign_role("alice", "admin")
acl.assign_role("bob", "reader")

while True:
    print("\n1. Create Role")
    print("2. Grant Permission")
    print("3. Assign Role")
    print("4. Check Permission")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        acl.create_role(input("Role Name: "))

    elif choice == "2":
        role = input("Role: ")
        permission = input("Permission: ")

        acl.grant_permission(role, permission)

    elif choice == "3":
        user = input("Username: ")
        role = input("Role: ")

        acl.assign_role(user, role)

    elif choice == "4":
        user = input("Username: ")
        permission = input("Permission: ")

        if acl.authorize(user, permission):
            print("ACCESS GRANTED")
        else:
            print("ACCESS DENIED")

    elif choice == "5":
        break
