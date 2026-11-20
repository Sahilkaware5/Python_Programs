"""Q2: DA, HRA, gross salary, tax and net salary.

Assumptions: DA = 40% of basic, HRA = 20% of basic,
tax = 10% of gross salary.
"""

basic = float(input("Enter basic salary: "))

da = 0.40 * basic
hra = 0.20 * basic
gross = basic + da + hra
tax = 0.10 * gross
net = gross - tax

print(f"\nBasic salary : {basic:.2f}")
print(f"DA (40%)     : {da:.2f}")
print(f"HRA (20%)    : {hra:.2f}")
print(f"Gross salary : {gross:.2f}")
print(f"Tax (10%)    : {tax:.2f}")
print(f"Net salary   : {net:.2f}")
