# Password Strength Checker

A simple command-line Python script to validate whether an entered password meets basic security criteria.

### Validation Rules:
* **Length:** Between 8 and 20 characters
* **Uppercase:** At least one uppercase letter (`A-Z`)
* **Lowercase:** At least one lowercase letter (`a-z`)
* **Digits:** At least one numerical digit (`0-9`)

### How It Works:
- Takes user input via CLI and trims whitespace using `.strip()`.
- Iterates through characters to flag uppercase, lowercase, and numeric presence using string methods (`isupper()`, `islower()`, `isdigit()`).
- Evaluates combined conditions to output whether the password is strong or weak along with requirement hints.

### Run the Script:
```bash
python main.py