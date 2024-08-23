import json

task_list = []
task_status = {}

def load_list():
    """Show ToDo.json file"""
    try:
        with open("E:/Programming/Python/JSON/ToDo.json", 'r') as file:
            task_status = json.load(file)
            task_list = list(task_status.keys())
    except FileNotFoundError:
        print("The ToDo list does not exist")

def add_task(task):
    """Add task to list"""
    task_list.append(task)


def add_status():
    global task_status
    """Task is completed or pending"""
    task_status = dict.fromkeys(task_list)
    print("Enter 1 for completed and 0 for pending.")
    for todos in task_status.keys():
        print(todos,":  ", end="")
        status = int(input())
        if status == 1:
            task_status[todos] = "completed"
        elif status == 0:
            task_status[todos] = "pending"
    print(task_status)

def save_tasks():
    """Saves tasks into json file"""
    with open("E:/Programming/Python/JSON/ToDo.json", 'w') as file:
        print(task_status)
        json.dump(task_status, file)
        
def work():
    print("""
    Enter 0 to add task
    Enter 1 to show ToDo list
    Enter 2 to save and exit
    Enter 3 to add or update status""")
    choice = int(input())
    match (choice):
        case 0:
            print("Enter 'n' anytime to exit")
            task = ""
            while(task != 'n'):
                task = input('Enter your task: ')
                if task != 'n':
                    add_task(task.strip().lower())
            work()
        case 1:
            i = 1
            for todos in task_list:
                print(f"{i}. {todos}")
                i+=1
            work()

        case 2:
            save_tasks()

        case 3:
            add_status()
            work()

        case _:
            print("Invalid Input") 

print("Welcome to My ToDo List Application")
load_list()
work()


