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
- Loops
"""

print("=" * 50)
print("          USERNAME VALIDATOR")
print("=" * 50)

username = input("Enter a username: ").strip()

if len(username) < 5 or len(username) > 15:
    print("❌ Username must be between 5 and 15 characters.")
elif not username[0].isalpha():
    print("❌ Username must start with a letter.")
elif " " in username:
    print("❌ Username must not contain spaces.")
elif not username.replace("_", "").isalnum():
    print("❌ Username can only contain letters, numbers, and underscores (_).")
else:
    print("✅ Username is valid.")