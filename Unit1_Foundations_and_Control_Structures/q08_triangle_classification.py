"""Q8: Validate a triangle and classify it."""

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sides must be positive numbers.")
elif a + b > c and a + c > b and b + c > a:
    print("Valid triangle.")
    if a == b == c:
        print("Type: Equilateral")
    elif a == b or b == c or a == c:
        print("Type: Isosceles")
    else:
        print("Type: Scalene")
else:
    print("Not a valid triangle (sum of any two sides must exceed the third).")
