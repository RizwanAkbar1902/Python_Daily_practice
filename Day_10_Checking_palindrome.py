"""
Day 10: Palindrome Checker

Author: Rizwan Akbar

Description:
This program checks whether a given word is a palindrome.
A palindrome is a word that reads the same forwards and
backwards, such as "madam", "level", or "racecar".

Concepts Used:
- Strings
- User Input
- String Slicing
- Conditional Statements (if-else)
"""

print("=" * 50)
print("          PALINDROME CHECKER")
print("=" * 50)

word = input("Enter a word: ").strip().lower()

if word == word[::-1]:
    print(f'\n✅ "{word}" is a palindrome.')
else:
    print(f'\n❌ "{word}" is not a palindrome.')