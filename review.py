#Exercise-1 

fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    print(fruit)

#Exercise-1.1

num = 1
fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    print(f"{num}. {fruit}")
    num += 1

#Exercise-2

scores = {"Rahul": 85, "Priya": 92, "Amit": 78}
for name, score in scores.items():
    print(f"{name} scored {score}")

# I have a question about the code. Like how did "Rahul" got assigned to name and then 85 got assigned to score in the for loop?

#Exercise-3

def multiply (a, b):
    return a * b

result = multiply(5, 8)
print(f"The result of multiplying 5 and 8 is: {result}")

#Exercise-4

fruits = []
num = 1

while True:
    user_input = input("Enter a number 1 to add a fruit, 2 to view the list, or 3 to exit: ")

    if user_input == "1":
        fruit = input("Enter a fruit to add: ")
        fruits.append(fruit)
        print(f"{fruit} has been added to the list.")
    elif user_input == "2":
        if not fruits:
            print("The list is empty.")
        else:
            print("Fruits in the list:")
            for fruit in fruits:
                print(f"{num}. {fruit}")
                num += 1
            num = 1  # Reset num for the next time the list is viewed
    elif user_input == "3":
        print("Exiting...")
        break
    else:
        print("Invalid input. Please try again.")
