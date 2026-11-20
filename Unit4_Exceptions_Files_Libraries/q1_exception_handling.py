"""Unit 4 - Q1: Exception Handling"""

# 1. ZeroDivisionError + ValueError with multiple except blocks, else, finally
print("=== Division with multiple except blocks ===")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: cannot divide by zero.")
except ValueError:
    print("Error: please enter valid integers only.")
else:
    print("Result =", result, "(no exception occurred)")
finally:
    print("finally block: always executes.\n")

# 2. IndexError
print("=== Invalid list index ===")
items = [10, 20, 30]
try:
    idx = int(input(f"Enter index to access (list has {len(items)} items): "))
    print("Element:", items[idx])
except IndexError:
    print("Error: index out of range.")
except ValueError:
    print("Error: index must be an integer.")
else:
    print("Index access succeeded.")
finally:
    print("finally block: list check complete.\n")

# 3. raise for age < 18
print("=== Using raise ===")
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above to be eligible.")
except ValueError as e:
    print("Exception:", e)
else:
    print("Eligible. Age accepted:", age)
finally:
    print("Program finished.")
