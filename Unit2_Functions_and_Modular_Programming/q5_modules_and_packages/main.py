"""Unit 2 - Q5: Using user-defined modules and packages"""

# 1. Import the entire module
import arithmetic

# 2. Import selected functions
from arithmetic import multiply, divide

# 3. Import the package and its modules
import student
from student import details, results

print("=== Entire module import ===")
print("arithmetic.add(10, 5)      =", arithmetic.add(10, 5))
print("arithmetic.subtract(10, 5) =", arithmetic.subtract(10, 5))

print("\n=== from ... import ===")
print("multiply(10, 5) =", multiply(10, 5))
print("divide(10, 5)   =", divide(10, 5))

print("\n=== Package: student ===")
info = details.get_details("Sahil Kaware", 101, "MCA")
details.display_details(info)

print()
results.display_result("Sahil Kaware", [85, 78, 92, 88, 90])

print("\n=== Functions exposed through __init__.py ===")
student.display_details(student.get_details("Riya Patil", 102, "BCA"))
print("Grade for 68%:", student.get_grade(68))
