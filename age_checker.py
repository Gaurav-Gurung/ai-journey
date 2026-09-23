age = int(input("Please enter your age: "))

if age <18:
    print("You are a minor.")
elif age >=21 and age <60:
    print("You are an adult and you can drink and drive.")
elif age>=60:
    print("You are a senior citizen and you can check out our senior citizen benefits.")
else:
    print("You are a young adult. You can vote and drive, but cannot drink yet.")