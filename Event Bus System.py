class EventBus:

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        self.subscribers.setdefault(event_type, []).append(handler)
        print("Subscribed successfully!")

    def unsubscribe(self, event_type, handler_name):
        handlers = self.subscribers.get(event_type, [])
        self.subscribers[event_type] = [
            h for h in handlers if h.__name__ != handler_name
        ]

    def publish(self, event_type, payload):
        handlers = self.subscribers.get(event_type, [])

        if not handlers:
            print("No subscribers found!")
            return

        for handler in handlers:
            handler(payload)


def send_email(payload):
    print("Email Service:", payload)


def update_analytics(payload):
    print("Analytics Service:", payload)


def audit_log(payload):
    print("Audit Log:", payload)


bus = EventBus()

bus.subscribe("user.created", send_email)
bus.subscribe("user.created", audit_log)
bus.subscribe("order.placed", update_analytics)

while True:
    print("\n1. Publish User Created")
    print("2. Publish Order Placed")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        bus.publish("user.created", {
            "user_id": 101,
            "email": "user@example.com"
        })

    elif choice == "2":
        bus.publish("order.placed", {
            "order_id": 501,
            "amount": 799
        })

    elif choice == "3":
        break
