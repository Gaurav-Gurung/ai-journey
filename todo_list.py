# My first todo list application in Python

tasks = []

while True:
    user_input = input("Please choose one of the following options: 1. Add a task 2. View tasks 3. Mark task as done 4. Remove task 5. Exit ")

    if user_input == "1":
        task_name = input("Task name: ")
        if task_name == "":
            print("Task name cannot be empty.")
        else:
            new_task = {}
            new_task["name"] = task_name
            new_task["done"] = False
            tasks.append(new_task)
            print(f"Task '{task_name}' added.")

    elif user_input == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            number = 1
            for task in tasks:
                if task["done"]:
                    status = "[X]"
                else:
                    status = "[ ]"
                print(f"{number}. {status} {task['name']}")
                number += 1

    elif user_input == "3":
        if len (tasks) == 0:
            print("No tasks to mark.")
        else:
            num = 1
            for task in tasks:
                if task["done"]:
                    status = "[X]"
                else:
                    status = "[ ]"
                print(f"{num}. {status} {task['name']}")
                num += 1

            pick = int(input("Which task number to mark done? "))
            if 1 <= pick <= len(tasks):
                task = tasks[pick - 1]
                task["done"] = True
                print(f"Task {pick} marked as done.")
            else:
                print("Invalid task number.")

    elif user_input == "4":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            num = 1
            for task in tasks:
                print(f"{num}. {task['name']}")
                num += 1

            pick = int(input("Which task number to remove? "))
            if 1 <= pick <= len(tasks):
                removed_task = tasks[pick - 1]
                tasks.remove(removed_task)
                print(f"Task '{removed_task['name']}' removed.")
            else:
                print("Invalid task number.")

    elif user_input == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid input.")
