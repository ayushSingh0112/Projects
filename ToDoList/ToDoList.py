import json
import os

class ToDo:
    def __init__(self, file_path):
        self.task_list = []
        self.task_status = {}
        self.file_path = file_path
        self.load_list()

    def load_list(self):
        """Load JSON file"""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write('{}')
        with open(self.file_path, 'r') as file:
            self.task_status = json.load(file)

    def empty_list(self):
        print("The task list is empty.\nPlease enter some tasks first.")

    def add_task(self, task):
        """Add task to list"""
        if task in list(self.task_status.keys()):
            print(f"The task {task} already exists.")
        elif task =="":
            print("Empty task. Enter a task.")
        else:
            self.task_status.setdefault(task, "pending")
        
    def add_status(self):
        """Task is completed or pending"""
        if self.task_status:
            print("Default status of tasks is pending.")
            print("Enter 1 for completed and 0 for pending")
            print("Task (current status) : (new status)")
            for todos in self.task_status.keys():
                while True:
                    print(f"{todos} ({self.task_status[todos]}) : ", end="")
                    try:
                        status = int(input())
                        if status == 1:
                            self.task_status[todos] = "completed"
                            break
                        elif status == 0:
                            self.task_status[todos] = "pending"
                            break
                        else:
                            print("Invalid input. Status remains unchanged.")
                    except ValueError:
                        print("Please enter either 0 or 1.")
            print("Status Updated Successfully.")
        else:
            self.empty_list()

    def save_tasks(self):
        """Saves tasks into json file"""
        with open(self.file_path, 'w') as file:
            json.dump(self.task_status, file)
        print("Saved successsfully.")
    
    def show_todo(self):
        """Show all the tasks"""
        if self.task_status:
            print("Tasks --> Status")
            i = 1
            for task, status in self.task_status.items():
                print(f"{i}. {task} --> {status}")
                i = i + 1
        else:
            self.empty_list()

    def del_todo(self):
        if self.task_status:
            print("Do you really want to delete all tasks: ")
            while True:
                confirm = input("Enter 'y' for yes and 'n' for no: ")
                if confirm == 'y':
                    self.task_status.clear()
                    print("Deleted all tasks successfully.")
                    break
                elif confirm == 'n':
                    print("Tasks not deleted.")
                    break
                else:
                    print("Invalid input.")
        else:
            self.empty_list()

    def del_task(self):
        if self.task_status:
            for i, task in enumerate(list(self.task_status.keys()), 1):
                print(f"{i}. {task}")
            while True:
                del_task = input("Enter name of the task to delete: ").strip().lower() 
                if del_task in list(list(self.task_status)):
                    del self.task_status[del_task]
                    print("Task Deleted Successfully.")
                    break
                else:
                    print("There is no such task\nPlease enter a valid task name.")
        else:
            self.empty_list()

    def work(self):
        """main function"""
        while True:
            print("""
            Enter 0 to add a new task
            Enter 1 to show ToDo list
            Enter 2 to add or update status
            Enter 3 to delete a single task
            Enter 4 to delete all tasks
            Enter 5 to save and exit
            Enter 6 to exit without saving
            """)
            choice = int(input())
            match (choice):
                case 0:
                    print("Enter 'n' anytime to exit")
                    while True:
                        task = input("Enter your task: ").strip().lower()
                        if task == 'n':
                            break
                        self.add_task(task)
                case 1:
                    self.show_todo()
                case 2:
                    self.add_status()
                case 3:
                    self.del_task()
                case 4:
                    self.del_todo()
                case 5:
                    self.save_tasks()
                    break
                case 6:
                    print("Exiting without saving")
                    break
                case _:
                    print("Invalid Input") 

print("Welcome to My ToDo List Application")
file_path = ""
todo_list = ToDo(file_path)