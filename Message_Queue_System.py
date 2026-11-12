from collections import deque


class MessageQueue:

    def __init__(self):
        self.messages = deque()
        self.counter = 1

    def enqueue(self, message):
        data = {
            "id": self.counter,
            "message": message
        }

        self.counter += 1
        self.messages.append(data)

        print("Message added!")

    def dequeue(self):
        if not self.messages:
            print("Queue is empty!")
            return None

        return self.messages.popleft()

    def size(self):
        return len(self.messages)


class Worker:

    def __init__(self, name, queue):
        self.name = name
        self.queue = queue

    def process(self):
        message = self.queue.dequeue()

        if message is None:
            return

        print(self.name, "processed:", message)


queue = MessageQueue()
worker = Worker("Worker-1", queue)

while True:
    print("\n1. Add Message")
    print("2. Process Message")
    print("3. Queue Size")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        queue.enqueue(input("Enter message: "))

    elif choice == "2":
        worker.process()

    elif choice == "3":
        print("Pending Messages:", queue.size())

    elif choice == "4":
        break
