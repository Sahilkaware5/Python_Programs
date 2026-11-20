"""Q10: Positive / negative / zero and even / odd."""

n = int(input("Enter an integer: "))

if n == 0:
    print("The number is zero (and even).")
else:
    sign = "positive" if n > 0 else "negative"
    parity = "even" if n % 2 == 0 else "odd"
    print(f"The number is {sign} and {parity}.")
