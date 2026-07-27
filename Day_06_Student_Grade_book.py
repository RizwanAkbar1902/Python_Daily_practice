student = {"Samreen": 95, "Rizwan": 79, "Usman": 89, "Ambreen": 99}

choice = 0
while choice != 4:
    print("-> Type '1' to search student.")
    print("-> Type '2' to add new student.")
    print("-> Type '3' to display all students.")
    print("-> Type '4' to Exit.")
    print("_" * 25)
    print()

    # Safely handle non-integer menu inputs
    user_input = input("Enter a choice: ").strip()
    if not user_input.isdigit():
        print("Invalid input! Please enter a number between 1 and 4.\n")
        print("=" * 50)
        print()
        continue

    choice = int(user_input)

    if choice == 1:
        st_name = input("Enter a name of student: ").strip().capitalize()
        if st_name in student:
            if student[st_name] >= 80:
                print(f"\n{student[st_name]} -> Passed.")
            else:
                print(f"\n{student[st_name]} -> Need Improvement.")
            print("=" * 50)
            print()
        else:
            print("\nStudent not found!\n")

    elif choice == 2:
        new_student = input("Enter a new student: ").strip().capitalize()
        
        # Check if student already exists
        if new_student in student:
            print(f"Note: {new_student} already exists. Updating grade...")

        new_grade = int(input("Enter new grade: "))
        student[new_student] = new_grade
        print("Student added/updated successfully!")
        print("=" * 50)
        print()

    elif choice == 3:
        print("\nThis is the record of all Students:\n")
        for name, grade in student.items():
            print(f"{name}: {grade}")
        print("=" * 50)
        print()

    elif choice == 4:
        print("Good bye!")
        print("_" * 50)
        print()

    else:
        print("Please enter a valid input between 1-4\n")
        print("=" * 50)
        print()