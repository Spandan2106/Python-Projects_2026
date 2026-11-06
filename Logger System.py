class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []

        return cls._instance

    def log(self, level, message):
        entry = level + ": " + message
        self.logs.append(entry)
        print(entry)

    def info(self, message):
        self.log("INFO", message)

    def warning(self, message):
        self.log("WARNING", message)

    def error(self, message):
        self.log("ERROR", message)

    def display_logs(self):
        for entry in self.logs:
            print(entry)


logger = Logger()

while True:
    print("\n1. INFO")
    print("2. WARNING")
    print("3. ERROR")
    print("4. Display Logs")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice in ["1", "2", "3"]:
        message = input("Enter message: ")

        if choice == "1":
            logger.info(message)
        elif choice == "2":
            logger.warning(message)
        else:
            logger.error(message)

    elif choice == "4":
        logger.display_logs()

    elif choice == "5":
        break
