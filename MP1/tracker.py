from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name": "",
    "due": None,  # datetime
    "lastActivity": None,  # datetime
    "description": "",
    "done": False  # False if not done, datetime otherise
}


# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()


def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")

    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")


def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i + 1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")


# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy()  # don't delete this
    try:
        # update lastActivity with the current datetime value
        task["lastActivity"] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

        # set the name, description, and due date (all must be provided)
        # due date must match one of the formats mentioned in str_to_datetime()
        task["name"] = name
        task["description"] = description
        task["due"] = str_to_datetime(due).strftime("%m/%d/%Y %H:%M:%S")

        # add the new task to the tasks list
        tasks.append(task)

        # make sure save() is still called last in this function
        save()

        # output a message confirming the new task was added or if the addition was rejected due to missing data
        print("new task added!")
        print(task)

    except Exception as e:
        print("new task rejected!")
        print(str(e))

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # ucid = vr76
    # date = 20/02/2023
    # solution:
    # 1. updated lastActivity with the current datetime using strftime function from datetime.now()
    # 2. assigned name, description and due date values to task Dict
    # 3. for due date used str_to_datetime function for validating the format
    # 4. appended the new task to tasks List()
    # 5. used try-except for displaying message of confirmation or rejection
    # 6. save() function remains same it the end
    # 7. ucid and implemented date has been added


def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        # get the task by index
        task = tasks[index]

        # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
        print()
        print("Existing values:")
        print("name: " + task["name"])
        print("description: " + task["description"])
        print("due: " + task["due"])

        name = input(f"What's the name of this task? (TODO name) \n").strip()
        desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
        update_task(index, name=name, description=desc, due=due)
    except IndexError:
        print("Given index is not available in Tasks list!")
    except Exception as e:
        print(str(e))
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # ucid = vr76
    # date = 20/02/2023
    # solution:
    # 1. fetched task from tasks list with given index value
    # 2. used try-except for displaying message for index out of bounds scenarios
    # 3. used print statements for showing existing value of each property where the TODOs are marked
    # 4. ucid and implemented date has been added


def update_task(index: int, name: str, description: str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        flag = False
        # find the task by index
        task = tasks[index]

        # update incoming task data if it's provided (if it's not provided use the original task property value)
        if name not in [None, ""]:
            flag = True
            task["name"] = name
        if description not in [None, ""]:
            flag = True
            task["description"] = description
        if due not in [None, ""]:
            flag = True
            task["due"] = str_to_datetime(due).strftime("%m/%d/%Y %H:%M:%S")

        # output that the task was updated if any items were changed, otherwise mention task was not updated
        if flag:
            # update lastActivity with the current datetime value
            task["lastActivity"] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

            tasks[index] = task

            # make sure save() is still called last in this function
            save()

            print("Task was updated!")
            print(task)
        else:
            print("Task not updated!")

    except IndexError:
        print("Given index is not available in Tasks list!")
    except Exception as e:
        print(str(e))
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # ucid = vr76
    # date = 20/02/2023
    # solution:
    # 1. fetched task from tasks list with given index value
    # 2. used try-except for displaying message for index out of bounds scenarios
    # 3. Updated name, description and due only if its provided
    # 4. updated lastActivity with the current datetime using strftime function from datetime.now()
    # 5. used a flag to check and print message
    # 6.save() function remains same it the end
    # 7. ucid and implemented date has been added


def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        # find task from list by index
        task = tasks[index]

        # if it's not done, record the current datetime as the value
        # if it is done, print a message saying it's already completed
        if not task["done"]:
            task["done"] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            tasks[index] = task

            # make sure save() is still called last in this function
            save()
        else:
            print("It's already completed")

    except IndexError:
        print("Given index is not available in Tasks list!")
    except Exception as e:
        print(str(e))

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # ucid = vr76
    # date = 20/02/2023
    # solution:
    # 1. fetched task from tasks list with given index value
    # 2. used try-except for displaying message for index out of bounds scenarios
    # 3. record the current datetime as the value if done is False
    # 4. Printed Message if done is not False
    # 5.save() function remains same it the end
    # 6. ucid and implemented date has been added



def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {}
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    save()


def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = []
    list_tasks(_tasks)


def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = []
    list_tasks(_tasks)


def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {}


# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit",
                "done"]


def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")


def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while (True):
        opt = input("What would you like to do?\n").strip()  # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num - 1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num - 1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num - 1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num - 1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num - 1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()


if __name__ == "__main__":
    run()