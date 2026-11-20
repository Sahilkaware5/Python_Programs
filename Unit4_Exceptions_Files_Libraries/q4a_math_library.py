"""Unit 4 - Q4(a): math library"""
import math

n = float(input("Enter a number: "))
print("Square root :", math.sqrt(n))
print("Power (n^3) :", math.pow(n, 3))
print("Ceiling     :", math.ceil(n))
print("Floor       :", math.floor(n))
k = int(input("Enter a non-negative integer for factorial: "))
print(f"Factorial of {k} :", math.factorial(k))
