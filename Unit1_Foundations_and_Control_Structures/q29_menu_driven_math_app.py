"""Q29: Menu-driven mathematical application."""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    return str(abs(n)) == str(abs(n))[::-1]


def is_armstrong(n):
    digits = len(str(n))
    return n == sum(int(d) ** digits for d in str(n))


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    a, b, series = 0, 1, []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


while True:
    print("\n===== MATH MENU =====")
    print("1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Thank you! Exiting...")
        break
    elif choice in ("1", "2", "3", "4", "5"):
        n = int(input("Enter a number: "))
        if choice == "1":
            print(f"{n} is {'' if is_prime(n) else 'not '}a prime number.")
        elif choice == "2":
            print(f"{n} is {'' if is_palindrome(n) else 'not '}a palindrome.")
        elif choice == "3":
            print(f"{n} is {'' if is_armstrong(n) else 'not '}an Armstrong number.")
        elif choice == "4":
            if n < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {n} = {factorial(n)}")
        else:
            print("Fibonacci series:", *fibonacci(n))
    else:
        print("Invalid choice! Please select between 1 and 6.")
