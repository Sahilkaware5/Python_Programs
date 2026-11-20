"""Q21: Number guessing game."""

import random

secret = random.randint(1, 100)
attempts = 0
print("I have picked a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess > secret:
        print("Too high! Try again.")
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
