"""Unit 4 - Q5: Command-Line Arguments

Usage:   python q5_command_line_args.py <num1> <operator> <num2>
Example: python q5_command_line_args.py 10 + 5
Note: on some shells '*' must be quoted, e.g.  python q5_command_line_args.py 10 "*" 5
"""
import sys

if len(sys.argv) != 4:
    print("Usage: python q5_command_line_args.py <num1> <operator> <num2>")
    print('Example: python q5_command_line_args.py 10 "*" 5')
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    op = sys.argv[2]
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: both numbers must be valid numeric values.")
    sys.exit(1)

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Error: division by zero.")
        sys.exit(1)
    result = num1 / num2
else:
    print("Invalid operator. Use +, -, * or /")
    sys.exit(1)

print(f"{num1} {op} {num2} = {result}")
