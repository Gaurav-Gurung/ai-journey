def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

user_input = int(input("Please enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius: "))

if user_input == 1:
    celsius = float(input("Please enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
elif user_input == 2:
    fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
else:
    print("Invalid input. Please enter 1 or 2.")    