"""
Project: Phonebook Manager
Day: 16
Author: Rizwan Akbar

Description:
A simple console-based Phonebook Manager that allows users
to add, search, view, and delete contacts using a dictionary.

Concepts Practiced:
- Dictionary
- While Loop
- Conditional Statements
- User Input
- Dictionary Methods
"""

# Dictionary to store contacts
phonebook = {}

while True:
    print("\n" + "=" * 40)
    print("         PHONEBOOK MANAGER")
    print("=" * 40)
    print("1. Add Contact")
    print("2. Find Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    print("=" * 40)

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        name = input("Enter contact name: ").strip().title()
        number = input("Enter phone number: ").strip()

        phonebook[name] = number
        print(f"\n✅ Contact '{name}' added successfully!")

    elif choice == "2":
        name = input("Enter contact name to search: ").strip().title()

        if name in phonebook:
            print(f"\n📞 {name}: {phonebook[name]}")
        else:
            print("\n❌ Contact not found.")

    elif choice == "3":
        if phonebook:
            print("\n------ Contact List ------")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("\n📭 Phonebook is empty.")

    elif choice == "4":
        name = input("Enter contact name to delete: ").strip().title()

        if name in phonebook:
            phonebook.pop(name)
            print(f"\n🗑️ Contact '{name}' deleted successfully!")
        else:
            print("\n❌ Contact not found.")

    elif choice == "5":
        print("\n" + "=" * 40)
        print(" Thank you for using Phonebook Manager!")
        print(" Goodbye! 👋")
        print("=" * 40)
        break

    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 5.")