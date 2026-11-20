"""Unit 3 - Q3: List Operations and List Comprehension"""

n = int(input("How many numbers? "))
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]
print("\nList created:", numbers)

# insert / remove at positions
pos = int(input("\nPosition to insert at: "))
val = int(input("Value to insert: "))
numbers.insert(pos, val)
print("After insert():", numbers)

pos = int(input("Position of element to remove (pop): "))
removed = numbers.pop(pos)
print(f"Removed {removed} using pop():", numbers)

# sort
print("\nAscending :", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

# max, min, sum
print("\nMax:", max(numbers), "| Min:", min(numbers), "| Sum:", sum(numbers))

# concatenation, repetition, indexing, membership
other = [100, 200]
print("\nConcatenation :", numbers + other)
print("Repetition    :", other * 3)
print("numbers[0]    :", numbers[0], "| numbers[-1]:", numbers[-1])
print("100 in other  :", 100 in other, "| 5 not in other:", 5 not in other)

# list comprehension
print("\nEven numbers :", [x for x in numbers if x % 2 == 0])
print("Odd numbers  :", [x for x in numbers if x % 2 != 0])
print("Squares      :", [x ** 2 for x in numbers])

# list methods
print("\n--- List methods ---")
demo = [3, 1, 2]
demo.append(4);        print("append(4)   :", demo)
demo.extend([9, 8]);   print("extend      :", demo)
demo.insert(1, 50);    print("insert(1,50):", demo)
demo.remove(50);       print("remove(50)  :", demo)
print("pop()       :", demo.pop(), "->", demo)
demo.sort();           print("sort()      :", demo)
demo.reverse();        print("reverse()   :", demo)
