import json
from pathlib import Path
DATA_FILE = Path("tasks.json")
def load_tasks():
  if not DATA_FILE.exists():
    return []
  with DATA_FILE.open("r", encoding="utf-8") as file:
    return json.load(file)
def save_tasks(tasks):
  with DATA_FILE.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=2)
def show_tasks(tasks):
  if not tasks:
    print("\nNo tasks found.")
    return
  print("\nYour Tasks:")
  for index, task in enumerate(tasks, start=1):
    status = "x" if task["done"] else " "
    print(f"{index}. [{status}] {task['title']}")
def add_task(tasks):
  title = input("Enter task title: ").strip()
  if not title:
    print("Task title cannot be empty.")
    return
  tasks.append({"title": title, "done": False})
  save_tasks(tasks)
  print("Task added.")

def toggle_task(tasks):
  show_tasks(tasks)
  if not tasks:
    return
  try:
    num = int(input("Enter task number to toggle done/undone: "))
    if 1 <= num <= len(tasks):
      tasks[num - 1]["done"] = not tasks[num - 1]["done"]
      save_tasks(tasks)
      print("Task updated.")
    else:
      print("Invalid task number.")
  except ValueError:
    print("Please enter a valid number.")


def delete_task(tasks):
  show_tasks(tasks)
  if not tasks:
    return
  try:
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
      removed = tasks.pop(num - 1)
      save_tasks(tasks)
      print(f"Deleted: {removed['title']}")
    else:
      print("Invalid task number.")
  except ValueError:
    print("Please enter a valid number.")


def main():
  tasks = load_tasks()
  while True:
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Toggle task status")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
      show_tasks(tasks)
    elif choice == "2":
      add_task(tasks)
    elif choice == "3":
      toggle_task(tasks)
    elif choice == "4":
      delete_task(tasks)
    elif choice == "5":
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Pick 1 to 5.")
if __name__ == "__main__":
  main()
