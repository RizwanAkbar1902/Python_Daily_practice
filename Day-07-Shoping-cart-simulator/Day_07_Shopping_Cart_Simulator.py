# Project: Shopping Cart Simulator
# Author: Rizwan Akbar
# Description: An interactive CLI shopping cart system to add, remove, and view items with quantity tracking.

print("========================================")
print("        Shopping Cart Simulator         ")
print("========================================")

cart = {}
choice = 0

while choice != 4:
    print("\n1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Exit")
    print("-" * 25)

    user_input = input("Enter your choice (1-4): ").strip()

    if not user_input.isdigit():
        print("\nInvalid input! Please enter a number between 1 and 4.")
        continue

    choice = int(user_input)

    # 1. Add Item
    if choice == 1:
        item = input("Enter item name: ").strip().capitalize()
        if not item:
            print("Item name cannot be empty!")
            continue

        qty_input = input(f"Enter quantity for {item}: ").strip()
        if qty_input.isdigit() and int(qty_input) > 0:
            quantity = int(qty_input)
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
            print(f"[✓] {quantity} {item}(s) added to cart!")
        else:
            print("[!] Invalid quantity. Must be a positive number.")

    # 2. Remove Item
    elif choice == 2:
        if cart:
            r_item = input("Enter item to remove: ").strip().capitalize()
            if r_item in cart:
                qty_remove = input(f"How many '{r_item}' to remove? (Current: {cart[r_item]}): ").strip()
                if qty_remove.isdigit() and int(qty_remove) > 0:
                    qty = int(qty_remove)
                    if qty >= cart[r_item]:
                        cart.pop(r_item)
                        print(f"[✓] All {r_item}(s) removed from cart.")
                    else:
                        cart[r_item] -= qty
                        print(f"[✓] Removed {qty} {r_item}(s). Remaining: {cart[r_item]}")
                else:
                    print("[!] Invalid number entered.")
            else:
                print(f"[!] '{r_item}' is not found in the cart.")
        else:
            print("[!] Your cart is already empty.")

    # 3. View Cart
    elif choice == 3:
        print("\n--- Current Shopping Cart ---")
        if cart:
            total_items = sum(cart.values())
            for item, qty in cart.items():
                print(f"- {item:<15}: {qty}")
            print("-" * 30)
            print(f"Total Unique Items : {len(cart)}")
            print(f"Total Item Quantity: {total_items}")
        else:
            print("Your cart is empty.")

    # 4. Exit
    elif choice == 4:
        print("\nThank you for shopping! Goodbye!")

    else:
        print("\n[!] Please select a valid option (1-4).")