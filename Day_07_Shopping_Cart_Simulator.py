print("          Shopping Cart Simulator          ")
cart = {}  # Changed variable name from 'dictionary' to 'cart'
choice = 0

while choice != 4:
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter Item name: ").strip().capitalize()
        quantity = int(input("Enter quantity: "))
        
        # Add to existing quantity if already in cart
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} {item}(s) added to cart!\n")

    elif choice == 2:
        # Check if cart is NOT empty
        if cart:
            R_item = input("Enter item to remove: ").strip().capitalize()
            if R_item in cart:
                cart.pop(R_item)
                print("Item removed successfully!\n")
            else:
                print("This item is not found in the cart.\n")
        else:
            print("No items in the cart yet!\n")

    elif choice == 3:
        print("\nViewing cart.....")
        if cart:
            for item, qty in cart.items():
                print(f"- {item}: {qty}")
        else:
            print("Your cart is empty.")
        print()

    elif choice == 4:
        print("\nGood bye!")

    else:
        print("\nInvalid input... Please enter 1-4.\n")