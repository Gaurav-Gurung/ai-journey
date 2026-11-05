# Task 1: Variables and F-Strings (The Basics)
# Create a variable called hero and set it to "Gaurav". Create a variable called power and set it to 100.
# Print exactly this sentence using an f-string:
# Gaurav has 100 power points.

hero = "Gaurav"
power = 100
print(f"{hero} has {power} power points.")

# Task 2: The for Loop and Lists
# Create a list of three fruits. Use a for loop to print each fruit.
# Bonus: Make the loop print the position number next to the fruit (e.g., 1. Apple, 2. Banana).

fruits = ["Apple", "Mango", "Banana"]

for i, fruits in enumerate(fruits, start=1):
    print(f"{i}. {fruits}")

# Task 3: Functions and Dictionaries

# Create a function called create_profile.

# It should take two parameters: name and age.

# Inside the function, create a dictionary with the keys "name" and "age".

# The function should return that dictionary.

# Call the function with your name and age, save it in a variable called my_profile, and print it.

def create_profile():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    profile = {"name": name, "age": age}
    return profile

my_profile = create_profile()
print(f"Name: {my_profile['name']}")
print(f"Age: {my_profile['age']}")

# Task 4: The "Traffic Cop" (Loops and Input)
# Write a while True loop.

# Ask the user: "Enter a command (or 'quit' to exit): "

# If they type "hello", print "Hi there!"

# If they type "quit", break the loop.

# Otherwise, print "I don't understand."

while True:
    user_input = input("Enter a command (or 'quit' to exit): ")

    if user_input == "hello":
        print("Hi there!")
    elif user_input == "quit":
        break
    else:
        print("I don't understand.")