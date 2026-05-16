tasks = []

def show_menu():
    print("\n===== Academic Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Update Task Status")
    print("5. Delete Task")
    print("6. Exit")


def add_task():
    course = input("Enter course name: ")
    task_type = input("Enter task type (Assignment/Quiz/Mid/Terminal/Project): ")
    status = input("Enter status (Pending/Ongoing/Completed): ")

    task = {
        "course": course,
        "type": task_type,
        "status": status
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\n===== All Tasks =====")

        for task in tasks:
            print("Course:", task["course"])
            print("Task Type:", task["type"])
            print("Status:", task["status"])
            print("-------------------")


def search_task():
    search_name = input("Enter course name to search: ")

    found = False

    for task in tasks:
        if task["course"].lower() == search_name.lower():

            print("\nTask Found!")
            print("Course:", task["course"])
            print("Task Type:", task["type"])
            print("Status:", task["status"])

            found = True

    if found == False:
        print("Task not found.")


def update_status():
    course_name = input("Enter course name to update: ")

    found = False

    for task in tasks:
        if task["course"].lower() == course_name.lower():

            new_status = input("Enter new status: ")

            task["status"] = new_status

            print("Status updated successfully!")

            found = True

    if found == False:
        print("Task not found.")


def delete_task():
    course_name = input("Enter course name to delete: ")

    found = False

    for task in tasks:
        if task["course"].lower() == course_name.lower():

            tasks.remove(task)

            print("Task deleted successfully!")

            found = True
            break

    if found == False:
        print("Task not found.")


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        search_task()

    elif choice == "4":
        update_status()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")