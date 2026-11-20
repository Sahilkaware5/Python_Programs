"""Q11: Loan eligibility.

Conditions: age 21-60, monthly income >= 25000, credit score >= 700.
"""

age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
score = int(input("Enter credit score: "))

if 21 <= age <= 60 and income >= 25000 and score >= 700:
    print("Congratulations! You are ELIGIBLE for the loan.")
else:
    print("Sorry, you are NOT eligible for the loan.")
    if not 21 <= age <= 60:
        print(" - Age must be between 21 and 60.")
    if income < 25000:
        print(" - Monthly income must be at least 25000.")
    if score < 700:
        print(" - Credit score must be at least 700.")
