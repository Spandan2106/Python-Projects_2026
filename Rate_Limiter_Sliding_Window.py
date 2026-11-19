import time
from collections import defaultdict, deque

class SlidingWindowRateLimiter:
    def __init__(self, limit=5, window_size_seconds=60):
        self.limit = limit
        self.window_size = window_size_seconds
        # client_id -> deque of timestamps
        self.requests = defaultdict(deque)

    def allow_request(self, client_id):
        current_time = time.time()
        window_start = current_time - self.window_size
        
        client_history = self.requests[client_id]

        # Evict timestamps outside the current sliding window
        while client_history and client_history[0] < window_start:
            client_history.popleft()

        # Check if the client has exceeded the limit
        if len(client_history) < self.limit:
            client_history.append(current_time)
            return True, f"Request allowed. Current usage: {len(client_history)}/{self.limit}"
        else:
            return False, f"Rate limit exceeded. Try again later."

# --- Example Usage ---
if __name__ == "__main__":
    # Allow 3 requests per 5 seconds window
    limiter = SlidingWindowRateLimiter(limit=3, window_size_seconds=5)
    client = "user_abc"

    print(f"--- Simulating request bursts for '{client}' ---")
    for i in range(1, 6):
        allowed, msg = limiter.allow_request(client)
        print(f"Request {i}: {msg}")
        time.sleep(0.5)
    print("\n--- Waiting for 5 seconds window to slide... ---")
    time.sleep(5)
    allowed, msg = limiter.allow_request(client)
    print(f"Request after waiting: {msg}")
