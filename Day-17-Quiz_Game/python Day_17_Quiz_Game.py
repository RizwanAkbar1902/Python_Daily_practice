"""
Project: Quiz Game
Day: 17
Author: Rizwan Akbar

Description:
A console-based Python quiz game containing 10 multiple-choice questions.
The program validates user input, checks answers, calculates the final score,
and provides performance feedback.

Key Feature:
If the user enters an invalid option, the same question is shown again
until a valid choice (A, B, C, or D) is entered.

Concepts Practiced:
- Lists
- Dictionaries
- For Loops
- While Loops
- Conditional Statements
- Functions
- User Input Validation
- String Methods
- Score Calculation
"""

questions = [
    {
        "question": "📝 1. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. func"],
        "answer": "B"
    },
    {
        "question": "📝 2. Which data type is used to store True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "📝 3. What is the output of 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "📝 4. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "📝 5. Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "📝 6. Which loop is commonly used to iterate through a sequence?",
        "options": ["A. for", "B. repeat", "C. loop", "D. iterate"],
        "answer": "A"
    },
    {
        "question": "📝 7. What does len() return?",
        "options": [
            "A. The data type",
            "B. The length of an object",
            "C. The last item",
            "D. The largest value"
        ],
        "answer": "B"
    },
    {
        "question": "📝 8. Which operator is used for exponentiation in Python?",
        "options": ["A. ^", "B. //", "C. **", "D. %%"],
        "answer": "C"
    },
    {
        "question": "📝 9. Which keyword is used to handle exceptions?",
        "options": ["A. catch", "B. error", "C. except", "D. handle"],
        "answer": "C"
    },
    {
        "question": "📝 10. What is the result of 10 % 3?",
        "options": ["A. 1", "B. 3", "C. 5", "D. 2"],
        "answer": "A"
    }
]


def display_question(question_data):
    """Display a question and its available options."""
    print(question_data["question"])

    for option in question_data["options"]:
        print("📌", option)

    print("-" * 50)


def get_valid_answer():
    """Keep asking until the user enters a valid option."""
    while True:
        user_answer = input("👉 Enter a choice (A/B/C/D): ").strip().upper()

        if user_answer in ("A", "B", "C", "D"):
            return user_answer

        print("⚠️ Invalid input! Please enter A, B, C, or D.\n")


def run_quiz():
    """Run the quiz and calculate the user's final score."""
    score = 0
    correct_answers = 0

    for question_data in questions:
        display_question(question_data)

        user_answer = get_valid_answer()

        if user_answer == question_data["answer"]:
            print("✅ Correct choice!")
            score += 10
            correct_answers += 1
        else:
            print("❌ Wrong choice.")
            print("💡 Correct option is:", question_data["answer"])

        print()

    print("~" * 50)
    print("              🏆 QUIZ COMPLETE 🏆")
    print("~" * 50)

    print(f"\n🎯 Correct answers: {correct_answers}/10")
    print(f"🎯 Total score: {score}/100")
    print("_" * 50)

    if score >= 90:
        print("🏆 Remarks: Excellent!")
    elif score >= 80:
        print("👏 Remarks: Great job!")
    elif score >= 60:
        print("📚 Remarks: Keep practicing!")
    else:
        print("💪 Remarks: More practice needed!")

    print("~" * 50)
    print("|       👋 Thanks for Playing!       |")
    print("~" * 50)
    print()


# Start the quiz
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("                 🎮 QUIZ GAME 🎮")
    print("=" * 50)
    print()

    run_quiz()