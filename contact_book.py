#contact_book.py - my first contact book app

contact_book = {}

while True:
    user_input = int(input("1. Add a contact, 2. View all contacts, 3. Search contact, 4. Delete contact, 5. Edit contact, 6. Exit: "))
    
    if user_input == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        if phone == "":
            print("Phone cannot be empty. Contact not added.")
        else:
            contact_book[name] = phone     
            print(f"{name} added.")

    elif user_input == 2:
        if len(contact_book) == 0:
            print("No contacts added yet.")
        else:
            for name, phone in contact_book.items():
                print(f"{name} : {phone}")

    elif user_input == 3:
        name = input("Name to search: ")
        if name in contact_book:
            print(f"{name}'s number : {contact_book[name]}")
        else:
            print("Contact not found.")

    elif user_input == 4:
        name = input("Name to delete: ")
        if name in contact_book:
            del contact_book[name]
            print(f"{name} deleted.")
        else:
            print("User not found.")

    elif user_input == 5:
        name = input("Name to Edit: ")
        if name in contact_book:
            new_phone = input("New Phone: ")
            if new_phone == "":
                print("Phone cannot be empty. Contact not updated.")
            elif new_phone != "":
                contact_book[name] = new_phone    
                print(f"{name}'s number updated to {new_phone}.")
        else:
            print("User not found.")
    
    elif user_input == 6:
        print("Goodbye!")
        break
    else:
        print("Please select the correct menu option number")

