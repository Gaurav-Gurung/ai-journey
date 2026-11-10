import random
choices = ["Rock", "Paper", "Scissors"]


print("Welcome to Rock, Paper, Scissors!")

while True:
    computer_choice = random.choice(choices)

    user_input = input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors) or q to exit: ")

    if user_input == 'q':
        print("Thanks for playing!")
        break
    elif user_input == '1':
        user_choice = "Rock"
    elif user_input == '2':
        user_choice = "Paper"   
    elif user_input == '3':
        user_choice = "Scissors"
    else:
        print("Wrong input. Please enter 1, 2, 3 or q to exit.")
        continue

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors"):
        print("You win!")
    elif (user_choice == "Rock" and computer_choice == "Paper"):
        print("You Loose!")
    elif (user_choice == "Paper" and computer_choice == "Rock"):
        print("You win!")
    elif (user_choice == "Paper" and computer_choice == "Scissors"):
        print("You Loose!")
    elif (user_choice == "Scissors" and computer_choice == "Rock"):
        print("You Loose!")
    elif (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!") 