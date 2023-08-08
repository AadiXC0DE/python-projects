import json
from termcolor import colored

class TodoApp:
    def __init__(self):
        self.tasks = []

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
        else:
            print(colored("Invalid task index", "red"))

    def list_tasks(self):
        if not self.tasks:
            print(colored("No tasks.", "yellow"))
        else:
            for index, task in enumerate(self.tasks):
                status = colored('Done', 'green') if task['completed'] else colored('Not Done', 'red')
                print(f"{index + 1}. {task['task']} - {status}")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
        else:
            print(colored("Invalid task index", "red"))

def main():
    todo_app = TodoApp()
    todo_app.load_tasks()

    while True:
        print("\nTodo App Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_app.add_task(task)
        elif choice == '2':
            todo_app.list_tasks()
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_app.complete_task(task_index)
        elif choice == '3':
            todo_app.list_tasks()
        elif choice == '4':
            todo_app.list_tasks()
            task_index = int(input("Enter the task index to delete: ")) - 1
            todo_app.delete_task(task_index)
        elif choice == '5':
            print("Saving and exiting Todo App.")
            todo_app.save_tasks()
            break
        else:
            print(colored("Invalid choice. Please select a valid option.", "red"))

if __name__ == "__main__":
    main()
