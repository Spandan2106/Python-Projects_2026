class Service:

    def __init__(self, name):
        self.name = name

    def handle(self, method, path, data):

        return {
            "service": self.name,
            "method": method,
            "path": path,
            "data": data,
            "status": 200
        }


class APIGateway:

    def __init__(self):
        self.routes = {}
        self.api_keys = set()

    def add_api_key(self, key):
        self.api_keys.add(key)

    def register_service(self, method, prefix, service):
        self.routes[(method.upper(), prefix)] = service

    def dispatch(self, key, method, path, data=None):

        if key not in self.api_keys:
            return {
                "status": 401,
                "error": "Unauthorized"
            }

        for (registered_method, prefix), service in self.routes.items():

            if (
                method.upper() == registered_method
                and path.startswith(prefix)
            ):
                return service.handle(method, path, data)

        return {
            "status": 404,
            "error": "Route not found"
        }


gateway = APIGateway()

gateway.add_api_key("demo-key")

gateway.register_service(
    "GET", "/users", Service("UserService")
)

gateway.register_service(
    "POST", "/orders", Service("OrderService")
)

while True:
    print("\n1. Send API Request")
    print("2. Exit")

    choice = input("Choice: ")

    if choice == "1":

        key = input("API Key: ")
        method = input("Method: ")
        path = input("Path: ")
        data = input("Payload: ")

        result = gateway.dispatch(
            key, method, path, data
        )

        print(result)

    elif choice == "2":
        break
