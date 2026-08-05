"""
Project: Smart Calculator
Day: 15
Author: Rizwan Akbar

Description:
A command-line Smart Calculator that performs basic arithmetic operations.
This project demonstrates the use of functions, loops, conditional
statements, exception handling, and user input validation.

Concepts Practiced:
- Functions
- Loops
- Conditional Statements
- Exception Handling
- User Input Validation
"""


# Function to add two numbers
def add(x, y):
    return x + y


# Function to subtract two numbers
def subtract(x, y):
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    return x * y


# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y


# Function to calculate power
def power(x, y):
    return x ** y


# Function to calculate remainder (modulus)
def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero is undefined."
    return x % y


# Main calculator function
def calculator():
    while True:
        print("\n" + "=" * 36)
        print("         SMART CALCULATOR")
        print("=" * 36)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Modulus (%)")
        print("7. Exit")
        print("=" * 36)

        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("\n" + "=" * 40)
            print(" Thank you for using Smart Calculator!")
            print(" Goodbye!")
            print("=" * 40)
            break

        if choice in ("1", "2", "3", "4", "5", "6"):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("\n[ERROR] Please enter valid numeric values.")
                continue

            print("-" * 40)

            if choice == "1":
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")

            elif choice == "2":
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == "3":
                print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")

            elif choice == "4":
                print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")

            elif choice == "5":
                print(f"Result: {num1}^{num2} = {power(num1, num2)}")

            elif choice == "6":
                print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")

            print("-" * 40)

        else:
            print("\n[ERROR] Invalid selection. Please choose an option from 1 to 7.")


# Run the application
if __name__ == "__main__":
    calculator()