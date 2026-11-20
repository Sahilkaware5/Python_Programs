"""Q13: ATM withdrawal simulation (correct PIN is 1234)."""

CORRECT_PIN = 1234

pin = int(input("Enter your PIN: "))
if pin != CORRECT_PIN:
    print("Incorrect PIN. Transaction cancelled.")
else:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount % 100 != 0:
        print("Amount must be a multiple of 100.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrawal successful! Please collect Rs. {amount:.2f}")
        print(f"Remaining balance: Rs. {balance:.2f}")
