my_contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    if name == "" or phone == "":
        print("Name and phone number cannot be empty. Contact not added.")
        return
    else:
        print(f"Adding contact: {name}, Phone: {phone}")
    contact = {"name": name, "phone": phone}
    my_contacts.append(contact)

def view_contacts():
    if not my_contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in my_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

while True:
    print("\nContact Management System")
    user_input = input("Enter 1 to add a contact, 2 to view contacts, or 3 to exit: ")

    if user_input == "1":
        add_contact()
    elif user_input == "2":
        view_contacts()
    elif user_input == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")