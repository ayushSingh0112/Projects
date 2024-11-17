import json
import time
import os
from plyer import notification
from datetime import datetime

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
            self.task_list = list(self.task_status.keys())
        self.work()

    def empty_list(self):
        print("The task list is empty.\nPlease enter some tasks first.")

    def add_task(self, task):
        """Add task to list"""
        if task in self.task_list:
            print(f"The task {task} already exists.")
        elif task =="":
            print("Empty task. Enter a task.")
        else:
            self.task_status.setdefault(task, "pending")
            self.task_list.append(task)
        
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
            print("-"*20 + "\nTasks --> Status\n" + "-"*20)
            i = 1
            for task, status in self.task_status.items():
                print(f"{i}. {task} --> {status}")
                i = i + 1
        else:
            self.empty_list()

    def del_todo(self):
        """Delete all ToDos"""
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
        """Delete Selected Task"""
        selected_task = self.select_task()
        self.task_list.remove(selected_task)
        del self.task_status[selected_task]
        print("Task Deleted Successfully.")

    def select_task(self):
        """Select a task from todo list"""
        self.show_todo()
        if self.task_status:
            task_no = int(input("Enter task number to select a task: "))
            try:
                selected_task = self.task_list[task_no-1]
            except IndexError:
                print("No such task. Select saved tasks")
                self.select_task()
            return selected_task
        
    def schedule (self, task, notification_time):
        """sets reminder for task"""
        while True:
            now = datetime.now().time()
            if now >= notification_time:
                notification.notify (
                    title = 'ToDo Reminder',
                    message = task,
                    timeout = 10,
                )
                break
            time.sleep(1)

    def work(self):
        """main function"""
        while True:
            print("-"*50)
            print("""
            Enter 0 to add a new task
            Enter 1 to show ToDo list
            Enter 2 to add or update status
            Enter 3 to delete a single task
            Enter 4 to delete all tasks
            Enter 5 to save and exit
            Enter 6 to exit without saving
            Enter 7 to set reminder for a task
            """)
            print("-"*50)
            choice = int(input("Enter Here: "))
            match (choice):
                case 0:
                    print("-"*30 + "Enter 'x' anytime to exit" + "-"*30)
                    while True:
                        task = input("Enter your task: ").strip().lower()
                        if task == 'x':
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
                    print("-"*30 + "Thanks for using." + "-"*30)
                    break
                case 6:
                    print("-"*30 + "Thanks for using." + "-"*30)
                    break
                case 7:
                    task = self.select_task()
                    if task: 
                        t = input("Enter time in 'HH:MM' format. For example, 09:36.\nEnter here: ")
                        print("Do not close the program before reminder.")
                        notification_time = datetime.strptime(t, "%H:%M").time() 
                        self.schedule(task, notification_time)
                case _:
                    print("Invalid Input") 

# Designing and Looks
print("*"*150)
print("*"*150)
app_name = "To-Do Applicaton"
credit = "Created By: Ayush Singh"
github = "GitHub: ayushSingh0112"
print(app_name.center(150))
print("*"*150)
print(credit + github.rjust(127))
print("*"*150)
print("Welcome to My ToDo List Application")

# To Do application 
file_path = "todo.json"
todo_list = ToDo(file_path)