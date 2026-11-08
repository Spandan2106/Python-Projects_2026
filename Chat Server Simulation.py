class User:

    def __init__(self, username):
        self.username = username
        self.inbox = []


class ChatServer:

    def __init__(self):
        self.users = {}

    def register_user(self, username):
        if username in self.users:
            print("User already exists!")
            return

        self.users[username] = User(username)
        print("User registered!")

    def send_message(self, sender, receiver, message):

        if sender not in self.users or receiver not in self.users:
            print("User not found!")
            return

        self.users[receiver].inbox.append({
            "sender": sender,
            "message": message
        })

        print("Message sent!")

    def receive_messages(self, username):

        if username not in self.users:
            print("User not found!")
            return

        inbox = self.users[username].inbox

        if not inbox:
            print("No messages!")
            return

        for msg in inbox:
            print(msg["sender"], ":", msg["message"])

        inbox.clear()


server = ChatServer()

while True:
    print("\n1. Register User")
    print("2. Send Message")
    print("3. Receive Messages")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        server.register_user(input("Username: "))

    elif choice == "2":
        sender = input("Sender: ")
        receiver = input("Receiver: ")
        message = input("Message: ")

        server.send_message(sender, receiver, message)

    elif choice == "3":
        username = input("Username: ")
        server.receive_messages(username)

    elif choice == "4":
        break
