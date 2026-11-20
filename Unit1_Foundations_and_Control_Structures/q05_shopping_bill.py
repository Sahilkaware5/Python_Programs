"""Q5: Subtotal, discount, GST and final payable amount for three products.

Assumptions: 10% discount if subtotal > 5000 else 5% if subtotal > 2000
else none; GST = 18% on the discounted amount.
"""

subtotal = 0
for i in range(1, 4):
    price = float(input(f"Enter price of product {i}: "))
    qty = int(input(f"Enter quantity of product {i}: "))
    subtotal += price * qty

if subtotal > 5000:
    discount = 0.10 * subtotal
elif subtotal > 2000:
    discount = 0.05 * subtotal
else:
    discount = 0

taxable = subtotal - discount
gst = 0.18 * taxable
final = taxable + gst

print(f"\nSubtotal       : {subtotal:.2f}")
print(f"Discount       : {discount:.2f}")
print(f"GST (18%)      : {gst:.2f}")
print(f"Final payable  : {final:.2f}")
