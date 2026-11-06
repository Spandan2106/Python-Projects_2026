import heapq

class TaskScheduler:

    def __init__(self):
        self.tasks = []
        self.counter = 0

    def add_task(self, name, priority):
        self.counter += 1

        heapq.heappush(
            self.tasks,
            (priority, self.counter, name)
        )

        print("Task added!")

    def execute_task(self):
        if not self.tasks:
            print("No pending tasks!")
            return

        priority, _, name = heapq.heappop(self.tasks)

        print("Executing:", name)
        print("Priority:", priority)

    def display_tasks(self):
        for priority, _, name in sorted(self.tasks):
            print(name, "- Priority:", priority)


scheduler = TaskScheduler()

while True:
    print("\n1. Add Task")
    print("2. Execute Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Task name: ")
        priority = int(input("Priority (1 = highest): "))
        scheduler.add_task(name, priority)

    elif choice == "2":
        scheduler.execute_task()

    elif choice == "3":
        scheduler.display_tasks()

    elif choice == "4":
        break
