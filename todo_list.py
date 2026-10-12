# My first todo list application in Python

tasks = []
number_of_tasks = 1

while True:
    user_input = input("Enter 1 to add a task, Enter 2 to view tasks, Enter 3 to mark task as complete, Enter 4 to remove task or Enter 5 to exit: ")

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

    elif user_input == "3":
        if len(tasks) == 0:
            print("No tasks to mark as complete.")
        else:
            print("Tasks in the list: ")
            for task in tasks:
                print(f" {number_of_tasks}. {task}")
                number_of_tasks += 1    

    elif user_input == "4":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("Tasks in the list: ")
            for task in tasks:
                print(f" {number_of_tasks}. {task}")
                number_of_tasks += 1
            task_to_remove = input("Enter the task name to remove: ")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print(f"Task '{task_to_remove}' removed from the list.")
            else:
                print(f"Task '{task_to_remove}' not found in the list.")                            
    elif user_input == "5":
        print("Exiting the application.")
        break   

    else:
        print("Invalid input. Please enter the right option.")