import time


class CircuitBreaker:

    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

    def __init__(self, threshold=3, timeout=5):
        self.threshold = threshold
        self.timeout = timeout

        self.failure_count = 0
        self.state = self.CLOSED
        self.opened_at = None

    def call(self, success):

        if self.state == self.OPEN:

            if time.time() - self.opened_at >= self.timeout:
                self.state = self.HALF_OPEN
                print("Circuit is HALF_OPEN!")
            else:
                print("Request rejected!")
                return

        if success:
            print("Service call successful!")

            self.failure_count = 0
            self.state = self.CLOSED
            self.opened_at = None

        else:
            print("Service call failed!")

            self.failure_count += 1

            if (
                self.failure_count >= self.threshold
                or self.state == self.HALF_OPEN
            ):
                self.state = self.OPEN
                self.opened_at = time.time()

                print("Circuit OPENED!")

    def status(self):
        print("Current State:", self.state)
        print("Failures:", self.failure_count)


breaker = CircuitBreaker()

while True:
    print("\n1. Simulate Success")
    print("2. Simulate Failure")
    print("3. Show Status")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        breaker.call(True)

    elif choice == "2":
        breaker.call(False)

    elif choice == "3":
        breaker.status()

    elif choice == "4":
        break
