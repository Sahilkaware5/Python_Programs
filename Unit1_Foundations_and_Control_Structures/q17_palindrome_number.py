"""Q17: Palindrome check using a while loop."""

n = int(input("Enter an integer: "))
num, rev = abs(n), 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if rev == abs(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
