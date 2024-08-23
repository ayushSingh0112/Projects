import json
def add_task(task):
    """Add task to list"""
    # global task_list
    task_list.append(task)

def save_tasks():
    """Saves tasks into json file"""
    with open("E:/Programming/Python/JSON/ToDo.json", 'w') as file:
        json.dump(task_list, file)

def load_list():
    """Show ToDo.json file"""
    try:
        with open("E:/Programming/Python/JSON/ToDo.json", 'r') as file:
            global task_list
            task_list = json.load(file)
    except FileNotFoundError:
        print("The ToDo list does not exist")

def work():
    print("""
    Enter 0 to add task
    Enter 1 to show ToDo list
    Enter 2 to save and exit""")
    choice = int(input())
    match (choice):
        case 0:
            while(True):
                task = input('Enter your task: ')
                add_task(task.strip().lower())
                if input("Press 'Enter' to continue\nEnter any key to exit: ").lower() == 'n':
                    break
            work()
        case 1:
            load_list()
            for todos in task_list:
                print(todos)
        case 2:
            save_tasks()

        case _:
            print("Invalid Input") 

print("Welcome to My ToDo List Application")
load_list()


