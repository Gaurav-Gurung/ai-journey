#shopping_list.py - my first shopping list app

shopping_list = []

while True:
    user_input = int(input("Please enter 1 to Add an item, 2 to view the list, 3 to Remove an item, 4 to exit: "))

    if user_input == 1:
        item = input("Please enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
    elif user_input == 2:
        print(shopping_list)
    elif user_input == 3: 
        item = input("Please enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")   
        else:
            print("Item not found in the list.")
    elif user_input == 4:
        break
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")