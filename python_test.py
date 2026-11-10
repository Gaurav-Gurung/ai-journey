orders = []

def add_order():
    customer_name = input("Enter customer name: ")
    if customer_name == "":
        print("Customer name cannot be empty. Please try again.")
        return
    print("Available pizza types: Margherita, Pepperoni, Veggie, BBQ Chicken")
    pizza_type = input("Enter Pizza type: ")
    qty = int(input("Enter quantity: "))
    order = {
        "customer_name": customer_name,
        "pizza_type": pizza_type,
        "quantity": qty
    }
    orders.append(order)
    print(f"Order has been added successfully: {order}")

def view_orders():
    if not orders:
        print("No orders have been placed yet.")
    else:
        print("Current Orders:")
        for order in orders:
            print(f"Customer: {order['customer_name']}, Pizza: {order['pizza_type']}, Quantity: {order['quantity']}")


while True:
    print("Welcome to the Pizza Ordering System")

    user_choice = input("Enter '1' to add an order, '2' to view orders, or 'q' to quit: ")
    if user_choice == '1':
        add_order()
    elif user_choice == '2':
        view_orders()
    elif user_choice.lower() == 'q':
        print("Exiting the Pizza Ordering System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")