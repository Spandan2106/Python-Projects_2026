import time

class RateLimiter:

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def allow_request(self):

        current_time = time.time()

        elapsed = current_time - self.last_refill

        new_tokens = elapsed * self.refill_rate

        self.tokens = min(
            self.capacity,
            self.tokens + new_tokens
        )

        self.last_refill = current_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True

        return False


# Main class
limiter = RateLimiter(5, 1)

while True:

    input("\nPress Enter to send a request...")

    if limiter.allow_request():
        print("Request Allowed!")
    else:
        print("Request Blocked! Rate limit exceeded.")
