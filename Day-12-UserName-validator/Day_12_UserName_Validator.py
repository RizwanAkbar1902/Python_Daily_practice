"""
Day 12: Username Validator

Author: Rizwan Akbar

Description:
This program validates a username based on basic rules.
The username must be between 5 and 15 characters,
start with a letter, contain no spaces, and may only
include letters, numbers, and underscores.

Concepts Used:
- Strings
- Conditional Statements
- String Methods
"""

print("=" * 50)
print("              USERNAME VALIDATOR")
print("=" * 50)

username = input("Enter a username: ").strip()

if not username:
    print("[ERROR] Username cannot be empty.")
elif len(username) < 5 or len(username) > 15:
    print("[ERROR] Username must be between 5 and 15 characters.")
elif not username[0].isalpha():
    print("[ERROR] Username must start with an alphabet letter.")
elif " " in username:
    print("[ERROR] Username must not contain spaces.")
elif not username.replace("_", "").isalnum():
    print("[ERROR] Username can only contain letters, numbers, and underscores (_).")
else:
    print(f"[SUCCESS] '{username}' is a valid username.")