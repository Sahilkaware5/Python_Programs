"""Q15: Mobile data bill.

Base plan Rs. 199 includes 5 GB.
Next 5 GB (5-10 GB)  : Rs. 20 / GB
Next 10 GB (10-20 GB): Rs. 15 / GB
Above 20 GB          : Rs. 10 / GB
"""

gb = float(input("Enter data usage in GB: "))

bill = 199
if gb > 5:
    bill += (min(gb, 10) - 5) * 20
if gb > 10:
    bill += (min(gb, 20) - 10) * 15
if gb > 20:
    bill += (gb - 20) * 10

print(f"Data used  : {gb} GB")
print(f"Total bill : Rs. {bill:.2f}")
