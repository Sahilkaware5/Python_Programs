"""Q3: Electricity bill using consumption slabs.

Slabs:  first 100 units   -> Rs. 3.00 / unit
        next 100 units    -> Rs. 5.00 / unit
        next 100 units    -> Rs. 7.00 / unit
        above 300 units   -> Rs. 9.00 / unit
"""

units = int(input("Enter units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    elif units <= 300:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    else:
        bill = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 9
    print(f"Units consumed : {units}")
    print(f"Electricity bill: Rs. {bill:.2f}")
