"""Q23: All prime numbers in a range, with their count."""

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

primes = []
for num in range(max(start, 2), end + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)

print(f"Prime numbers between {start} and {end}:")
print(*primes)
print("Total prime numbers found:", len(primes))
