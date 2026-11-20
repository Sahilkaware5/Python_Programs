"""Q20: Armstrong number check."""

n = int(input("Enter an integer: "))

digits = len(str(abs(n)))
temp, total = n, 0
while temp > 0:
    d = temp % 10
    total += d ** digits
    temp //= 10

if total == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
