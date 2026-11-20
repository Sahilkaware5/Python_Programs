"""Q26: GCD and LCM using iterative statements."""

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

x, y = a, b
while y != 0:           # Euclid's algorithm
    x, y = y, x % y
gcd = x
lcm = a * b // gcd

print("GCD:", gcd)
print("LCM:", lcm)
