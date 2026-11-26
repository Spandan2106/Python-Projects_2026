import time
import heapq
import threading
import random
from datetime import datetime
class Task:
    def __init__(self, task_id, priority, func, args=(), max_retries=3):
        self.task_id = task_id
        self.priority = priority  # Lower number = higher priority
        self.func = func
        self.args = args
        self.max_retries = max_retries
        self.retries = 0
    def __lt__(self, other):
        return self.priority < other.priority
class TaskScheduler:
    def __init__(self, num_workers=3):
        self.task_queue = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.num_workers = num_workers
        self.running = True
        self.workers = []
    def submit_task(self, task_id, priority, func, args=(), max_retries=3):
        task = Task(task_id, priority, func, args, max_retries)
        with self.condition:
            heapq.heappush(self.task_queue, task)
            self.condition.notify()
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Task '{task_id}' (Priority: {priority}) submitted.")
    def _worker_loop(self, worker_id):
        while self.running:
            task = None
            with self.condition:
                while not self.task_queue and self.running:
                    self.condition.wait(timeout=0.5)
                if not self.task_queue:
                    continue
                task = heapq.heappop(self.task_queue)

            if task:
                try:
                    print(f"[Worker-{worker_id}] Executing Task '{task.task_id}'...")
                    task.func(*task.args)
                    print(f"[Worker-{worker_id}] Task '{task.task_id}' completed successfully.")
                except Exception as e:
                    task.retries += 1
                    print(f"[Worker-{worker_id}] Task '{task.task_id}' failed (Attempt {task.retries}/{task.max_retries}): {e}")
                    if task.retries <= task.max_retries:
                        backoff = 2 ** task.retries
                        print(f"[Worker-{worker_id}] Re-queuing Task '{task.task_id}' with backoff {backoff}s...")
                        time.sleep(backoff)
                        with self.condition:
                            heapq.heappush(self.task_queue, task)
                            self.condition.notify()
                    else:
                        print(f"[Worker-{worker_id}] Task '{task.task_id}' permanently failed after max retries.")

    def start(self):
        for i in range(self.num_workers):
            worker = threading.Thread(target=self._worker_loop, args=(i + 1,), daemon=True)
            self.workers.append(worker)
            worker.start()
    def shutdown(self):
        self.running = False
        with self.condition:
            self.condition.notify_all()
        for worker in self.workers:
            worker.join()
        print("Task Scheduler shut down gracefully.")
if __name__ == "__main__":
    def sample_job(name, fail_prob=0.3):
        time.sleep(random.uniform(0.5, 1.5))
        if random.random() < fail_prob:
            raise RuntimeError("Simulated processing error")
        print(f"--> Job '{name}' finished execution.")
    scheduler = TaskScheduler(num_workers=2)
    scheduler.start()
    for i in range(1, 6):
        scheduler.submit_task(f"Task-{i}", priority=random.randint(1, 5), func=sample_job, args=(f"Task-{i}",))
    time.sleep(6)
    scheduler.shutdown()
