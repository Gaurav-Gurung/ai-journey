products = []

def add_product():
    name = input("Product Name: ")
    price = int(input("Price: "))
    stock = int(input("Stock: "))

    new_product = {
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(new_product)
    print(f"{name} added to inventory")

def view_products():
    if len(products) == 0:
        print("Inventory is empty")
        return
    else:
        for i, item in enumerate (products, start=1):
            print(f"{i}. {item['name']} - Price: {item['price']} - Stock: {item['stock']}")

def update_stock():
    if len(products) == 0:
        print("Inventory is empty.")
        return
    for i, item in enumerate(products, start=1):
        print(f"{i}. {item['name']} (Current stock: {item['stock']})")

    pick = int(input("Which product number to update? "))

    if 1 <= pick <= len(products):
        new_stock = int(input("Enter new stock amount: "))
        products[pick - 1]["stock"] = new_stock
        print("Stock updated.")
    else:
        print("Invalid product number.")



while True:
    user_input = input("Choose one from the menu - 1. Add Product, 2. View Product, 3. Update Stock, 4. Exit: ")

    if user_input == "1":
        add_product()
    elif user_input == "2":
        view_products()
    elif user_input == "3":
        update_stock()
    elif user_input == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Input.")