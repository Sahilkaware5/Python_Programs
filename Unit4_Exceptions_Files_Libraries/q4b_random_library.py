"""Unit 4 - Q4(b): random library"""
import random

print("Random integer (1-100)   :", random.randint(1, 100))
print("Random in range(0,50,5)  :", random.randrange(0, 50, 5))

fruits = ["apple", "banana", "mango", "orange", "grape"]
print("Random element from list :", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled list            :", fruits)
