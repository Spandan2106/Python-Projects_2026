class Server:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.active_requests = 0
        self.healthy = True

    def can_accept(self):
        return (
            self.healthy
            and self.active_requests < self.capacity
        )


class LoadBalancer:

    def __init__(self):
        self.servers = []
        self.pointer = 0

    def add_server(self, server):
        self.servers.append(server)

    def route_request(self, request_id):

        if not self.servers:
            print("No servers available!")
            return

        for _ in range(len(self.servers)):

            server = self.servers[self.pointer]

            self.pointer = (
                self.pointer + 1
            ) % len(self.servers)

            if server.can_accept():
                server.active_requests += 1

                print(
                    request_id,
                    "routed to",
                    server.name
                )

                return

        print("All servers are unavailable!")

    def complete_request(self, name):

        for server in self.servers:

            if server.name == name:
                if server.active_requests > 0:
                    server.active_requests -= 1
                    print("Request completed!")
                else:
                    print("No active requests!")
                return

        print("Server not found!")

    def display(self):

        for server in self.servers:
            print(
                server.name,
                "Active:", server.active_requests,
                "Capacity:", server.capacity,
                "Healthy:", server.healthy
            )


lb = LoadBalancer()

lb.add_server(Server("Server-A", 2))
lb.add_server(Server("Server-B", 2))
lb.add_server(Server("Server-C", 2))

while True:
    print("\n1. Route Request")
    print("2. Complete Request")
    print("3. Toggle Server Health")
    print("4. Display Servers")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        lb.route_request(input("Request ID: "))

    elif choice == "2":
        lb.complete_request(input("Server Name: "))

    elif choice == "3":
        name = input("Server Name: ")

        for server in lb.servers:
            if server.name == name:
                server.healthy = not server.healthy
                print("Health:", server.healthy)
                break
        else:
            print("Server not found!")

    elif choice == "4":
        lb.display()

    elif choice == "5":
        break
