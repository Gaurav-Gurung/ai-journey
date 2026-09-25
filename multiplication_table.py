#multiplication_table.py - my first multiplication table 

number = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    