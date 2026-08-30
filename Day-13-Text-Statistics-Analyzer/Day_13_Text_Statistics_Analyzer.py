"""
Day 13: Text Statistics Analyzer

Author: Rizwan Akbar

Description:
This program analyzes a user-entered sentence and
displays useful statistics such as the total number
of characters, words, vowels, consonants, digits,
and spaces.

Concepts Used:
- Strings
- Loops
- Conditional Statements
- String Methods
"""

print("=" * 55)
print("           TEXT STATISTICS ANALYZER")
print("=" * 55)

text = input("Enter a sentence: ")

characters = len(text)
words = len(text.split())

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print("\n" + "=" * 55)
print("                 RESULTS")
print("=" * 55)

print(f"Total Characters : {characters}")
print(f"Total Words      : {words}")
print(f"Total Vowels     : {vowels}")
print(f"Total Consonants : {consonants}")
print(f"Total Digits     : {digits}")
print(f"Total Spaces     : {spaces}")

print("\nThank you for using the Text Statistics Analyzer!")