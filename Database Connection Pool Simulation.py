class FakeConnection:

    def __init__(self, connection_id):
        self.connection_id = connection_id
        self.in_use = False

    def execute(self, query):
        print("Executing:", query)


class ConnectionPool:

    def __init__(self, size):
        self.connections = [
            FakeConnection(i + 1)
            for i in range(size)
        ]

    def acquire(self):

        for connection in self.connections:

            if not connection.in_use:
                connection.in_use = True

                print(
                    "Connection acquired:",
                    connection.connection_id
                )

                return connection

        print("Connection pool exhausted!")
        return None

    def release(self, connection):

        if connection not in self.connections:
            print("Invalid connection!")
            return

        if not connection.in_use:
            print("Connection already released!")
            return

        connection.in_use = False
        print("Connection released!")

    def status(self):

        for connection in self.connections:
            print(
                connection.connection_id,
                "IN USE" if connection.in_use else "FREE"
            )


pool = ConnectionPool(2)
leased = {}

while True:
    print("\n1. Acquire")
    print("2. Execute Query")
    print("3. Release")
    print("4. Show Pool")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        connection = pool.acquire()

        if connection:
            leased[connection.connection_id] = connection

    elif choice == "2":
        cid = int(input("Connection ID: "))

        connection = leased.get(cid)

        if connection:
            connection.execute(input("Query: "))
        else:
            print("Connection not leased!")

    elif choice == "3":
        cid = int(input("Connection ID: "))
        connection = leased.get(cid)

        if connection:
            pool.release(connection)

            if not connection.in_use:
                leased.pop(cid)

        else:
            print("Connection not found!")

    elif choice == "4":
        pool.status()

    elif choice == "5":
        break
