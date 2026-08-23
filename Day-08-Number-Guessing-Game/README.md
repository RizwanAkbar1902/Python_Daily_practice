\# Number Guessing Game (CLI) 🎯



A robust, console-based number guessing game built in Python featuring attempt limits, interactive feedback, and input validation.



\---



\## 📖 Overview



The program generates a pseudo-random integer between 1 and 100. The player has a maximum of 7 attempts to find the correct number, receiving real-time hints ("Too LOW" or "Too HIGH") after every round.



\---



\## 🚀 Key Features



\* \*\*Safe Input Handling\*\*: Uses `try / except ValueError` blocks to catch non-numeric inputs without crashing.

\* \*\*Range Validation\*\*: Verifies that guesses remain within the valid \[1, 100] boundary.

\* \*\*Loop Else Construct\*\*: Uses Python's `while...else` construct to handle the game-over condition when attempts run out.

\* \*\*Replay Mechanism\*\*: Prompts the user to restart or exit cleanly after each game round.



\---



\## 🛠️ Concepts Covered



\* `random.randint()` for number generation

\* Exception handling (`try / except`)

\* Nested `while` loops and loop control (`break`, `return`)

\* String normalization (`.strip().lower()`)



\---



\## 💻 How to Run



```bash

python Day\_08\_Number\_Guessing\_game.py

