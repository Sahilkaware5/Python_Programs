"""Q14: Income tax by slabs (annual income).

Up to 3,00,000   : nil
3,00,001-6,00,000: 5%
6,00,001-9,00,000: 10%
9,00,001-12,00,000: 15%
12,00,001-15,00,000: 20%
Above 15,00,000  : 30%
"""

income = float(input("Enter annual income: "))

slabs = [(300000, 0.00), (600000, 0.05), (900000, 0.10),
         (1200000, 0.15), (1500000, 0.20), (float("inf"), 0.30)]

tax = 0
lower = 0
for upper, rate in slabs:
    if income > lower:
        tax += (min(income, upper) - lower) * rate
    lower = upper

print(f"Annual income : Rs. {income:.2f}")
print(f"Tax payable   : Rs. {tax:.2f}")
