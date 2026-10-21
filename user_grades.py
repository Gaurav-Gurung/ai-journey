students = {}

def add_student():
    name = input("Enter the student's name: ")
    if name == "":
        print("Name cannot be empty.")
        return

    grades = {}
    
    while True:
        subject = input("Enter the subject (or type 9 to finish): ")

        if subject == "9":
            break
        if subject == "":
            print ("Subject cannot be empty.")
            continue
        grade = int(input(f"Enter the grade for {subject}: "))
        grades [subject] = grade

    students[name] = grades
    print(f"{name}'s grades saved.")

def view_students():
    if len(students) == 0:
        print("No students added yet.")
        return
    for name, grades in students.items():
        print(f"{name}:")
        for subject, grade in grades.items():
            print(f"  {subject}: {grade}")


# Main Menu

while True:
    print("\n1. Add a student")
    print("2. View all students")
    print("3. Exit")
    user_input = input("Choose an option: ")

    if user_input == "1":
        add_student()
    elif user_input == "2":
        view_students()
    elif user_input == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
