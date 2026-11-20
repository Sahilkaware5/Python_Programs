"""Q6: Grade from percentage using if-elif-else with validation."""

p = float(input("Enter percentage: "))

if p < 0 or p > 100:
    print("Invalid percentage! It must be between 0 and 100.")
elif p >= 90:
    print("Grade: A+ (Outstanding)")
elif p >= 80:
    print("Grade: A (Excellent)")
elif p >= 70:
    print("Grade: B (Very Good)")
elif p >= 60:
    print("Grade: C (Good)")
elif p >= 50:
    print("Grade: D (Satisfactory)")
elif p >= 40:
    print("Grade: E (Pass)")
else:
    print("Grade: F (Fail)")
