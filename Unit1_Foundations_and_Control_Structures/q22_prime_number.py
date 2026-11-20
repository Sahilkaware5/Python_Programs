"""Q22: Prime number check using a for loop."""

n = int(input("Enter an integer: "))

is_prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

print(f"{n} is a prime number." if is_prime else f"{n} is not a prime number.")
