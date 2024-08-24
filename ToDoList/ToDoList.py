import json

class ToDo:
    def __init__(self, file_path):
        self.task_list = []
        self.task_status = {}
        self.file_path = file_path
        self.load_list()

    def load_list(self):
        """Load JSON file"""
        try:
            with open(self.file_path, 'r') as file:
                self.task_status = json.load(file)
                self.task_list = list(self.task_status.keys())
        except FileNotFoundError:
            print("The ToDo list does not exist")

    def add_task(self, task):
        """Add task to list"""
        if task in list(self.task_status.keys()):
            print(f"The task {task} already exists.")
        else:
            self.task_status.setdefault(task, "pending")
        

    def add_status(self):
        """Task is completed or pending"""
        print("Default status of tasks is pending.")
        print("Enter 1 for completed and 0 for pending")
        print("Task (current status) : (new status)")
        for todos in self.task_status.keys():
            print(f"{todos} ({self.task_status[todos]}) : ", end="")
            status = int(input())
            if status == 1:
                self.task_status[todos] = "completed"
            elif status == 0:
                self.task_status[todos] = "pending"
        print("Status Updated Successfully.")

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
            print("No tasks are added.")
    def del_todo(self):
        self.task_status.clear()
        print("Deleted all tasks successfully")

    def work(self):
        """main function"""
        while True:
            print("""
            Enter 0 to add a new task
            Enter 1 to show ToDo list
            Enter 2 to save and exit
            Enter 3 to add or update status
            Enter 4 to exit without saving
            Enter 5 to delete all tasks
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
                    self.save_tasks()
                    break
                case 3:
                    self.add_status()
                case 4:
                    print("Exiting without saving")
                    break
                case 5:
                    self.del_todo()
                case _:
                    print("Invalid Input") 

print("Welcome to My ToDo List Application")
file_path = "E:/Programming/Python/JSON/ToDo.json"
todo_list = ToDo(file_path)
todo_list.work()