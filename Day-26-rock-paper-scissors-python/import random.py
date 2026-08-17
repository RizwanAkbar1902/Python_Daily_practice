import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("====================================")
    print("   ROCK, PAPER, SCISSORS GAME")
    print("====================================")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit.\n")

    while True:
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == "quit":
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid input! Please choose rock, paper, or scissors.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Check Winner
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round! 🎉\n")
            user_score += 1
        else:
            print("Computer wins this round! 🤖\n")
            computer_score += 1

        print(f"Current Score -> You: {user_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    play_rps()