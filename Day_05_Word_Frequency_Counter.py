# Word Frequency Counter
# Author: Rizwan Akbar
# Description: Counts how many times each word appears in a user-provided sentence.

import string


def clean_text(text):
    """Removes punctuation, converts text to lowercase, and splits into words."""
    # Convert all text to lowercase so 'Python' and 'python' match
    text = text.lower()

    # Remove punctuation marks like '.', ',', '!', etc.
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split the text into a list of words
    words = text.split()
    return words


def count_words(word_list):
    """Counts the frequency of each word using a simple loop and dictionary."""
    frequency_dict = {}

    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict


def display_results(frequency_dict):
    """Prints the word frequencies in a neat format."""
    print("\n--- Word Frequencies ---")

    for word in frequency_dict:
        count = frequency_dict[word]
        print(f"{word}: {count}")


def main():
    print("=== Simple Word Frequency Counter ===")
    user_input = input("Enter a sentence: ").strip()

    if user_input == "":
        print("You did not enter any text!")
        return

    # Step 1: Clean and split the sentence into words
    words = clean_text(user_input)

    # Step 2: Count the words
    frequencies = count_words(words)

    # Step 3: Print the results
    display_results(frequencies)


# Runs the main program
if __name__ == "__main__":
    main()