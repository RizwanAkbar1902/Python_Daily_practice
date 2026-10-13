class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder}: Rs. {amount} deposited successfully.")
            print(f"Current Balance: Rs. {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print(f"{self.account_holder}: Insufficient funds! Current Balance: Rs. {self.balance}")
        else:
            self.balance -= amount
            print(f"{self.account_holder}: Rs. {amount} withdrawn successfully.")
            print(f"Remaining Balance: Rs. {self.balance}")

    def check_balance(self):
        print(f"Account: {self.account_holder} | Available Balance: Rs. {self.balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create account
    user_account = BankAccount("Rizwan Akbar", 5000)

    # Initial balance check
    user_account.check_balance()

    # Deposit money
    user_account.deposit(2000)

    # Valid withdrawal
    user_account.withdraw(3000)

    # Invalid withdrawal (exceeding balance)
    user_account.withdraw(6000)