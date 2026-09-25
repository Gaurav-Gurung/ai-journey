#guess_the_number.py - my first guess the number game

number = 42

while True:
    guess = int(input("Guess the number:"))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Correct!")
        break