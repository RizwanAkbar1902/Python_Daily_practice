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


def find_most_frequent(frequency_dict):
    """Finds which word appeared the most number of times."""
    top_word = ""
    max_count = 0

    for word, count in frequency_dict.items():
        if count > max_count:
            max_count = count
            top_word = word

    return top_word, max_count


def display_results(frequency_dict, total_words):
    """Prints the summary and word frequencies in a neat format."""
    print("\n===============================")
    print("      WORD FREQUENCY REPORT    ")
    print("===============================")
    print(f"Total Words Count : {total_words}")
    print(f"Total Unique Words: {len(frequency_dict)}")
    print("-------------------------------")

    # Display individual word counts
    for word, count in frequency_dict.items():
        print(f"- {word:<15} : {count}")

    print("-------------------------------")
    
    # Show the most frequent word
    top_word, max_count = find_most_frequent(frequency_dict)
    if top_word:
        print(f"Most Frequent Word: '{top_word}' (appeared {max_count} times)")
    print("===============================\n")


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

    # Step 3: Print the results with summary
    display_results(frequencies, len(words))


# Runs the main program
if __name__ == "__main__":
    main()