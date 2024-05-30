class Task:
    def __init__(self, description, type):
        self.description = description
        self.type = type
        self.is_completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, type):
        task = Task(description, type)
        self.tasks.append(task)

    def delete_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Task not found.")

    def complete_task(self, index):
        if index < len(self.tasks):
            self.tasks[index].is_completed = True
        else:
            print("Task not found.")

    def edit_task(self, index, description=None, type=None):
        if index < len(self.tasks):
            if description:
                self.tasks[index].description = description
            if type:
                self.tasks[index].type = type
        else:
            print("Task not found.")

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.is_completed else "Not Completed"
            print(f"Task {i+1}: {task.description} (Type: {task.type}, Status: {status})")

# Create a new to-do list
my_todo_list = TodoList()

# Add tasks
my_todo_list.add_task("Buy groceries", "Personal")
my_todo_list.add_task("Finish project", "Work")

# Complete a task
my_todo_list.complete_task(0)

# Edit a task
my_todo_list.edit_task(1, "Complete project part 1")

# Delete a task
my_todo_list.delete_task(0)

# View tasks
my_todo_list.view_tasks()

# please work github
