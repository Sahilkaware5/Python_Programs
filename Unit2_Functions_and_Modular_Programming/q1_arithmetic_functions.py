"""Unit 2 - Q1: Functions and Function Arguments
Arithmetic operations using user-defined functions with positional,
keyword and default arguments.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b (handles division by zero)."""
    if b == 0:
        return "Error: division by zero"
    return a / b


def calculate(a, b, operation="add"):
    """Perform an operation; 'add' is the default argument value."""
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in operations:
        return "Invalid operation"
    return operations[operation](a, b)


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("\n--- Positional arguments ---")
    print(f"add({x}, {y})       = {add(x, y)}")
    print(f"subtract({x}, {y})  = {subtract(x, y)}")
    print(f"multiply({x}, {y})  = {multiply(x, y)}")
    print(f"divide({x}, {y})    = {divide(x, y)}")

    print("\n--- Keyword arguments (order does not matter) ---")
    print(f"subtract(b={y}, a={x}) = {subtract(b=y, a=x)}")
    print(f"divide(b={y}, a={x})   = {divide(b=y, a=x)}")

    print("\n--- Default argument (operation defaults to 'add') ---")
    print(f"calculate({x}, {y})                      = {calculate(x, y)}")
    print(f"calculate({x}, {y}, operation='multiply') = {calculate(x, y, operation='multiply')}")
