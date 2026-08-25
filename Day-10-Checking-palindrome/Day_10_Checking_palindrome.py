# Project: Palindrome Checker
# Author: Rizwan Akbar
# Description: A simple Python script to check whether a word, phrase, or number reads the same forwards and backwards.


def is_palindrome(text: str) -> bool:
    """Cleans the text and checks if it matches its reverse."""
    # Convert to lowercase and remove spaces
    cleaned_text = text.lower().replace(" ", "")

    # Reverse using string slicing [::-1]
    reversed_text = cleaned_text[::-1]

    return cleaned_text == reversed_text


def main():
    print("========================================")
    print("        PALINDROME CHECKER TOOL         ")
    print("========================================")
    print("Type any word/phrase to check, or 'exit' to quit.\n")

    while True:
        user_input = input("Enter text: ").strip()

        if user_input.lower() == "exit":
            print("\nThanks for using Palindrome Checker. Goodbye!")
            break

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        # Check result
        if is_palindrome(user_input):
            print(f" Result: '{user_input}' IS a palindrome! 🎉\n")
        else:
            print(f" Result: '{user_input}' is NOT a palindrome.\n")
        
        print("-" * 40)


if __name__ == "__main__":
    main()