class Notification:

    def __init__(self):
        self.history = []

    def send_email(self, user, message):
        print("Email sent to:", user)
        print("Message:", message)
        self.history.append(("EMAIL", user, message))

    def send_sms(self, user, message):
        print("SMS sent to:", user)
        print("Message:", message)
        self.history.append(("SMS", user, message))

    def send_push(self, user, message):
        print("Push notification sent to:", user)
        print("Message:", message)
        self.history.append(("PUSH", user, message))

    def show_history(self):
        for notification in self.history:
            print(notification)


service = Notification()

while True:
    print("\n1. Email")
    print("2. SMS")
    print("3. Push Notification")
    print("4. History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice in ["1", "2", "3"]:
        user = input("Enter recipient: ")
        message = input("Enter message: ")

        if choice == "1":
            service.send_email(user, message)
        elif choice == "2":
            service.send_sms(user, message)
        else:
            service.send_push(user, message)

    elif choice == "4":
        service.show_history()

    elif choice == "5":
        break
