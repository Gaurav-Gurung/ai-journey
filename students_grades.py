students = {
    "Harry": { "English": 85, "Math": 92, "Science": 78 },
    "Ron": { "English": 88, "Math": 76, "Science": 90 },
    "Hermione": { "English": 95, "Math": 98, "Science": 100 },
    "Draco": { "English": 70, "Math": 85, "Science": 80, "History": 75 }
}

while True:
    user_input = int(input("1. View all students, 2. View one student's grades, 3. Calculate average for a student, 4. Exit: "))

    if user_input == 1:
        if len(students) == 0:
            print("No students added yet.")
        else:
            for name, grades in students.items():
                print(f"{name}:  ")
                for subject, grade in grades.items():
                    print(f"  {subject}: {grade}")

    elif user_input == 2:
        name = input("Name of the student to view grades:")
        if name in students:
            grades = students[name]
            print(f"{name}'s grades:")      
            for subject, grade in grades.items():
                print(f"  {subject}: {grade}")
        else:
            print("Student not found.")

    elif user_input == 3:
        name = input("Name of the student to calculate average:")
        if name in students:
            grades = students[name]
            average = sum(grades.values()) / len(grades)
            print(f"{name}'s average grade: {average:.2f}")
        else:
            print("Student not found.")

    elif user_input == 4:
        print("Goodbye!")
        break   