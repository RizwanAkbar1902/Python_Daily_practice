# Palindrome Checker (Python) 🔄

A clean, interactive command-line Python utility to verify if a word, phrase, or number is a palindrome.

---

## 📖 What is a Palindrome?
A palindrome is a sequence of characters that reads the same backward as forward (e.g., `madam`, `racecar`, `1221`, `nurses run`).

---

## 🚀 Key Features

* **Case-Insensitive Checking**: Automatically converts input to lowercase so `Radar` and `radar` are treated identically.
* **Space-Insensitive**: Trims spaces using `.replace(" ", "")` to properly evaluate multi-word phrases.
* **Efficient Reversal**: Uses Python's fast slice notation `[::-1]` for sequence inversion.
* **Continuous Interactive Loop**: Allows testing multiple inputs in a single run.

---

## 🛠️ Concepts Covered

* **Functions & Return Types**: Defining reusable functions (`is_palindrome`) returning boolean values.
* **String Slicing**: Reversing strings via step slicing (`[::-1]`).
* **String Methods**: `.strip()`, `.lower()`, and `.replace()`.
* **Flow Control**: `while True`, `break`, and `continue`.

---

## 💻 How to Run

```bash
python Day_10_Checking_palindrome.py