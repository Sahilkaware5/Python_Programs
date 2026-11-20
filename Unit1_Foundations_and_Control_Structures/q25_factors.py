"""Q25: All factors of an integer and their count."""

n = int(input("Enter a positive integer: "))

factors = [i for i in range(1, n + 1) if n % i == 0]
print(f"Factors of {n}:", *factors)
print("Total number of factors:", len(factors))
