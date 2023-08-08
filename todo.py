class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
        else:
            print("Invalid task index")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(self.tasks):
                status = 'Done' if task['completed'] else 'Not Done'
                print(f"{index + 1}. {task['task']} - {status}")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index")

def main():
    todo_app = TodoApp()

    while True:
        print("\nTodo App Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Delete Task")
        print("5. Exit")

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
            print("Exiting Todo App.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
