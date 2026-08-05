"""
Day 14: Expense Tracker

Author: Rizwan Akbar

Description:
A simple console-based Expense Tracker that allows users
to add expenses, view recorded expenses, and calculate
the total amount spent.

Concepts Used:
- Dictionary
- While Loop
- Conditional Statements (if-elif-else)
- User Input
- Dictionary Methods
"""

print("=" * 50)
print("              EXPENSE TRACKER")
print("=" * 50)

expenses = {}
choice = 0

while choice != 4:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        item = input("Enter item name: ").strip().capitalize()
        amount = int(input("Enter expense amount: "))
        expenses[item] = amount
        print("✅ Expense added successfully!")

    elif choice == 2:
        if expenses:
            print("\n----- Expense List -----")
            for item, amount in expenses.items():
                print(f"{item}: Rs. {amount}")
        else:
            print("\nNo expenses recorded yet.")

    elif choice == 3:
        total = sum(expenses.values())
        print(f"\n💰 Total Expense: Rs. {total}")

    elif choice == 4:
        print("\nThank you for using Expense Tracker!")
        print("Goodbye! 👋")

    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 4.")