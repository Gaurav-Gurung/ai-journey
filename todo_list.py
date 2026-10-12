# My first todo list application in Python

tasks = []
number_of_tasks = 1

while True:
    user_input = input("Enter 1 to add a task, Enter 2 to view tasks, Enter 3 to mark task as complete or Enter 4 to exit: ")

    if user_input == "1":
        task_name = input("Enter the task name: ")
        if task_name == "":
            print("Task name cannot be empty. Task not added.")
        else:
            tasks.append(task_name)
            print(f"Task '{task_name}' added to the list.")

    elif user_input == "2":
        if len(tasks) == 0:
            print("No tasks added yet.")
        else:
            print("Tasks in the list: ")
            for task in tasks:
                print(f" {number_of_tasks}. {task}")
                number_of_tasks += 1

    elif user_input == "4":
        print("Exiting the application.")
        break   

    else:
        print("Invalid input. Please enter the right option.")