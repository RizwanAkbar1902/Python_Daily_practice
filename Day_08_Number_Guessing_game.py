"""
Day 08 - Number Guessing Game

Author: Rizwan Akbar

Description:
A console-based number guessing game where the player
has 7 attempts to guess a randomly generated number.
The project demonstrates functions, loops, exception
handling and the random module.
"""


import random


def get_user_guess():
    """Prompts user for input and handles non-integer errors safely."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print(
                    "[ERROR] Out of bounds! Please enter a number between 1 and 100."
                )
        except ValueError:
            print("[ERROR] Invalid input! Please enter a valid integer.")


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\n" + "=" * 45)
    print("      WELCOME TO THE NUMBER GUESSING GAME     ")
    print("=" * 45)
    print(f"I have chosen a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it right!\n")

    while attempts < max_attempts:
        attempts += 1
        print(f"--- Attempt {attempts}/{max_attempts} ---")

        guess = get_user_guess()

        if guess == secret_number:
            print(
                f"\n🎉 CONGRATULATIONS! You guessed the number {secret_number} in {attempts} attempts!"
            )
            break
        elif guess < secret_number:
            print("💡 Too LOW! Try a higher number.\n")
        else:
            print("💡 Too HIGH! Try a lower number.\n")
    else:
        print("\n❌ GAME OVER!")
        print(f"You ran out of attempts. The secret number was {secret_number}.")


def main():
    while True:
        play_game()

        while True:
            play_again = (
                input("\nDo you want to play again? (yes/no): ")
                .strip()
                .lower()
            )

            if play_again in ["yes", "y"]:
                break
            elif play_again in ["no", "n"]:
                print("\nThanks for playing! Goodbye 👋")
                return
            else:
                print("[ERROR] Invalid choice! Please enter yes or no.")

if __name__ == "__main__":
    main()