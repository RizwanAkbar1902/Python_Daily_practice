"""
Day 11: BMI Health Analyzer

Author: Rizwan Akbar

Description:
This program calculates the Body Mass Index (BMI)
using the user's height and weight. It then classifies
the BMI into different health categories and displays
a health suggestion.

Concepts Used:
- User Input
- Variables
- Arithmetic Operators
- Conditional Statements (if-elif-else)
"""

print("=" * 50)
print("           BMI HEALTH ANALYZER")
print("=" * 50)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
    print("Suggestion: Maintain a balanced diet and consult a healthcare professional if needed.")
elif bmi < 25:
    print("Category: Normal Weight")
    print("Suggestion: Great job! Maintain your healthy lifestyle.")
elif bmi < 30:
    print("Category: Overweight")
    print("Suggestion: Consider regular exercise and a balanced diet.")
else:
    print("Category: Obese")
    print("Suggestion: It is recommended to consult a healthcare professional and adopt a healthier lifestyle.")

print("\nThank you for using the BMI Health Analyzer!")