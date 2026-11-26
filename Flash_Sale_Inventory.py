import threading
import time
import random
class FlashSaleInventory:
    def __init__(self, stock_map):
        # item_id -> available_quantity
        self.inventory = stock_map
        self.locks = {item_id: threading.Lock() for item_id in stock_map}
        self.reservations = {}
    def reserve_item(self, user_id, item_id, quantity=1):
        if item_id not in self.inventory:
            return False, "Item does not exist."
        # Acquire lock specific to the item to handle concurrent purchases
        with self.locks[item_id]:
            if self.inventory[item_id] >= quantity:
                # Simulate database processing latency
                time.sleep(0.01)
                self.inventory[item_id] -= quantity
                
                if item_id not in self.reservations:
                    self.reservations[item_id] = []
                self.reservations[item_id].append({"user_id": user_id, "qty": quantity})
                
                return True, f"Successfully reserved {quantity} unit(s) of '{item_id}'."
            else:
                return False, f"Out of stock! Requested {quantity}, available {self.inventory[item_id]}."

class FlashSaleClientSimulator:
    def __init__(self, system, item_id):
        self.system = system
        self.item_id = item_id
    def simulate_user_purchase(self, user_id):
        success, message = self.system.reserve_item(user_id, self.item_id, quantity=1)
   
if __name__ == "__main__":
    # Initialize flash sale with 10 units of "LIMITED_EDITION_PHONE"
    sale_system = FlashSaleInventory({"LIMITED_EDITION_PHONE": 10})
    simulator = FlashSaleClientSimulator(sale_system, "LIMITED_EDITION_PHONE")
    threads = []
    total_users = 30  # 30 concurrent users trying to buy only 10 items
    print(f"Starting Flash Sale simulation with {total_users} users for 10 items...")
    start_time = time.time()
    for i in range(1, total_users + 1):
        t = threading.Thread(target=simulator.simulate_user_purchase, args=(f"User_{i}",))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"\n--- Flash Sale Completed in {time.time() - start_time:.4f}s ---")
    print(f"Remaining Inventory: {sale_system.inventory}")
    print(f"Total Successful Orders: {len(sale_system.reservations.get('LIMITED_EDITION_PHONE', []))}")
