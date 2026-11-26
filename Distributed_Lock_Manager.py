import time
import threading
import uuid

class DistributedLockManager:
    def __init__(self):
        self.locks = {}  # resource_id -> dict (lock metadata)
        self.global_lock = threading.Lock()

    def acquire_lock(self, resource_id, client_id, ttl_seconds=5):
        with self.global_lock:
            now = time.time()            
            # Check if lock exists and is expired
            if resource_id in self.locks:
                lock_info = self.locks[resource_id]
                if lock_info["expires_at"] < now:
                    # Expired, clean it up
                    del self.locks[resource_id]

            # Acquire lock if available
            if resource_id not in self.locks:
                fencing_token = self.locks.get(f"{resource_id}_counter", 0) + 1
                self.locks[f"{resource_id}_counter"] = fencing_token 
                self.locks[resource_id] = {
                    "client_id": client_id,
                    "expires_at": now + ttl_seconds,
                    "fencing_token": fencing_token
                }
                return True, fencing_token, "Lock acquired successfully."
            # Allow reentrant acquisition by the same client
            lock_info = self.locks[resource_id]
            if lock_info["client_id"] == client_id:
                lock_info["expires_at"] = now + ttl_seconds  # Refresh TTL
                return True, lock_info["fencing_token"], "Lock refreshed (reentrant)."
            return False, 0, f"Lock currently held by another client."
    def release_lock(self, resource_id, client_id, fencing_token):
        with self.global_lock:
            if resource_id not in self.locks:
                return False, "Lock does not exist or already expired."            
            lock_info = self.locks[resource_id]
            if lock_info["client_id"] != client_id:
                return False, "Unauthorized release: Client does not own the lock."   
            if lock_info["fencing_token"] != fencing_token:
                return False, "Fencing token mismatch (stale token)."
            del self.locks[resource_id]
            return True, "Lock released successfully."
# --- Example Usage ---
if __name__ == "__main__":
    dlm = DistributedLockManager()
    client_a = "worker_node_1"
    client_b = "worker_node_2"
    resource = "database_migration_lock"
    print("--- Client A attempts to acquire lock ---")
    success, token_a, msg = dlm.acquire_lock(resource, client_a, ttl_seconds=2)
    print(f"Result: {msg} | Fencing Token: {token_a}")
    print("\n--- Client B attempts to acquire the same lock immediately ---")
    success_b, _, msg_b = dlm.acquire_lock(resource, client_b, ttl_seconds=2)
    print(f"Result: {msg_b}")
    print("\n--- Waiting for Client A's lock lease to expire (2.5s)... ---")
    time.sleep(2.5)
    print("--- Client B attempts to acquire lock after expiration ---")
    success_b, token_b, msg_b = dlm.acquire_lock(resource, client_b, ttl_seconds=2)
    print(f"Result: {msg_b} | Fencing Token: {token_b}")
    print("\n--- Client B releases the lock ---")
    released, rel_msg = dlm.release_lock(resource, client_b, token_b)
    print(f"Result: {rel_msg}")
