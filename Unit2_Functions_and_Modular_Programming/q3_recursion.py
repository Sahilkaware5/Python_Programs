"""Unit 2 - Q3: Recursive Functions
Factorial and Fibonacci series using recursion.
"""


def factorial(n):
    """Return n! recursively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:      # base case
        return 1
    return n * factorial(n - 1)  # recursive case


def fibonacci(n):
    """Return the n-th Fibonacci number (0-indexed: 0, 1, 1, 2, 3, ...)."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_series(terms):
    """Return a list with the first `terms` Fibonacci numbers."""
    return [fibonacci(i) for i in range(terms)]


if __name__ == "__main__":
    num = int(input("Enter a number to find factorial: "))
    print(f"Factorial of {num} = {factorial(num)}")

    n = int(input("\nEnter number of terms for Fibonacci series: "))
    print(f"Fibonacci series ({n} terms):", *fibonacci_series(n))
