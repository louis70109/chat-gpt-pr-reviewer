import datetime
import logging

logging.basicConfig(level=logging.INFO)

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.created_date = datetime.datetime.now()

    def __str__(self):
        return f"Task: {self.name}, Description: {self.description}, Due Date: {self.due_date}"

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks[task.name] = task
            logging.info(f"Added task: {task}")
        else:
            logging.error("Invalid task object")

    def remove_task(self, name):
        if name in self.tasks:
            removed_task = self.tasks.pop(name)
            logging.info(f"Removed task: {removed_task}")
        else:
            logging.warning("Task not found")

    def list_tasks(self):
        if not self.tasks:
            logging.info("No tasks available")
        else:
            for name, task in self.tasks.items():
                logging.info(task)

    def find_task(self, name):
        task = self.tasks.get(name)
        if task:
            logging.info(f"Found task: {task}")
        else:
            logging.warning("Task not found")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Find task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(name, description, due_date)
            task_manager.add_task(task)
        elif choice == "2":
            name = input("Enter task name to remove: ")
            task_manager.remove_task(name)
        elif choice == "3":
            task_manager.list_tasks()
        elif choice == "4":
            name = input("Enter task name to find: ")
            task_manager.find_task(name)
        elif choice == "5":
            logging.info("Exiting the program...")
            break
        else:
            logging.error("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
