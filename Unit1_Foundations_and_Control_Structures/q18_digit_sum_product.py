"""Q18: Sum and product of digits using a while loop."""

n = abs(int(input("Enter an integer: ")))
total, product = 0, 1

if n == 0:
    product = 0
while n > 0:
    d = n % 10
    total += d
    product *= d
    n //= 10

print("Sum of digits    :", total)
print("Product of digits:", product)
