"""Q12: Admission eligibility.

Conditions: at least 50% in each of Maths, Physics, Chemistry and
at least 60% overall.  (Marks are out of 100.)
"""

maths = float(input("Enter marks in Mathematics: "))
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))

overall = (maths + physics + chemistry) / 3
print(f"Overall percentage: {overall:.2f}%")

if maths >= 50 and physics >= 50 and chemistry >= 50 and overall >= 60:
    print("Student is ELIGIBLE for admission.")
else:
    print("Student is NOT eligible for admission.")
