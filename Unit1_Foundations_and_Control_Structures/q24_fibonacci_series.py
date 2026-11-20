"""Q24: Fibonacci series using a for loop, with the sum of terms."""

n = int(input("Enter number of terms: "))

a, b = 0, 1
total = 0
series = []
for _ in range(n):
    series.append(a)
    total += a
    a, b = b, a + b

print("Fibonacci series:", *series)
print("Sum of terms    :", total)
