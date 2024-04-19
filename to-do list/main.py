class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print(f"Task '{deleted_task['task']}' has been removed.")
        else:
            print("Task number not found.")

    def list_tasks(self):
        if not self.tasks:
            print("There are no tasks currently.")
        else:
            print("Current Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"Task #{index + 1}: {task['task']} {'(completed)' if task['completed'] else ''}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task '{self.tasks[index]['task']}' marked as completed.")
        else:
            print("Task number not found.")

if __name__ == "__main__":
    todo_list = ToDoList()
    print("Welcome to the to-do list app :)")
    while True:
        print("\nPlease select one of the following options:")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. Mark a task as completed")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the number of the task to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter the number of the task to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")

