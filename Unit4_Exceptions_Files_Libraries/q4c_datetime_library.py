"""Unit 4 - Q4(c): datetime library"""
from datetime import datetime, date

now = datetime.now()
print("Current date and time:", now.strftime("%d-%m-%Y %H:%M:%S"))
print("Day  :", now.day)
print("Month:", now.month)
print("Year :", now.year)

d1 = input("\nEnter first date (YYYY-MM-DD): ")
d2 = input("Enter second date (YYYY-MM-DD): ")
date1 = datetime.strptime(d1, "%Y-%m-%d").date()
date2 = datetime.strptime(d2, "%Y-%m-%d").date()
diff = date2 - date1
print(f"Difference between the dates: {abs(diff.days)} days")
print("Days from first date until today:", (date.today() - date1).days)
