"""
Project: Bank Account Simulator
Day: 19
Author: Rizwan Akbar

Description:
A console-based bank account simulator built with Python's
Object-Oriented Programming (OOP) concepts. The program allows
bank accounts to perform deposits, withdrawals, and balance
management while handling invalid transactions safely.

Concepts Practiced:
- Classes and Objects
- Constructors
- Instance Attributes
- Methods
- Encapsulation
- Dictionaries
- Conditional Statements
- Input Validation
"""
# Simple Bank Account Simulator

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[SUCCESS] ${amount} deposited. New Balance: ${self.balance}")
        else:
            print("[ERROR] Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"[FAILED] Insufficient balance! Current Balance: ${self.balance}")
        elif amount <= 0:
            print("[ERROR] Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"[SUCCESS] ${amount} withdrawn. Remaining Balance: ${self.balance}")

    def display_info(self):
        print(f"Account #: {self.account_number} | Holder: {self.holder_name} | Balance: ${self.balance}")


# --- MAIN BANK SYSTEM LOGIC ---

def run_bank_system():
    # Dictionary to store accounts (Key: Account Number, Value: BankAccount Object)
    accounts = {}

    # Adding Sample Data
    accounts[1001] = BankAccount(1001, "Ali", 500)
    accounts[1002] = BankAccount(1002, "Sara", 1200)

    print("--- WELCOME TO PYTHON BANK SIMULATOR ---")

    # 1. Deposit money into Ali's account
    print("\n1. Depositing money for Ali...")
    accounts[1001].deposit(200)

    # 2. Withdraw money from Sara's account
    print("\n2. Withdrawing money for Sara...")
    accounts[1002].withdraw(500)

    # 3. Attempting to withdraw more than available balance (Should fail)
    print("\n3. Testing insufficient balance error...")
    accounts[1001].withdraw(1000)

    # 4. Display Final Account Details
    print("\n--- FINAL ACCOUNTS REPORT ---")
    for acc_num, account in accounts.items():
        account.display_info()


if __name__ == "__main__":
    run_bank_system()