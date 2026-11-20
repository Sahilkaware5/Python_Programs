"""Q19: Number of digits, largest and smallest digit using while loop."""

n = abs(int(input("Enter an integer: ")))

count = 0
largest = 0
smallest = 9

if n == 0:
    count = 1
while n > 0:
    d = n % 10
    count += 1
    if d > largest:
        largest = d
    if d < smallest:
        smallest = d
    n //= 10

if count == 1 and largest == 0 and smallest == 9:  # input was 0
    smallest = 0

print("Number of digits:", count)
print("Largest digit   :", largest)
print("Smallest digit  :", smallest)
