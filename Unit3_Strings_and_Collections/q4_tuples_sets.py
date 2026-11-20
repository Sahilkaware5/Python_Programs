"""Unit 3 - Q4: Tuples, Sets and Set Operations"""

# ---------- Tuples ----------
rolls = (101, 102, 103, 104, 105, 106)
print("Tuple elements:", end=" ")
for r in rolls:
    print(r, end=" ")
print()
print("Indexing rolls[0] =", rolls[0], "| rolls[-1] =", rolls[-1])
print("Slicing rolls[1:4] =", rolls[1:4])
print("Concatenation:", rolls + (107, 108))

# ---------- Sets ----------
course_a = {101, 102, 103, 104, 105}
course_b = {104, 105, 106, 107}
print("\nCourse A:", course_a)
print("Course B:", course_b)
print("Union                :", course_a | course_b)
print("Intersection         :", course_a & course_b)
print("Difference (A - B)   :", course_a - course_b)
print("Symmetric difference :", course_a ^ course_b)

small = {101, 102}
print("\n{101,102} is subset of A   :", small.issubset(course_a))
print("A is superset of {101,102}  :", course_a.issuperset(small))
print("B is subset of A            :", course_b.issubset(course_a))

course_a.add(110)
print("\nAfter add(110)    :", course_a)
course_a.remove(101)
print("After remove(101) :", course_a)
course_a.discard(999)  # no error if missing
print("After discard(999):", course_a)

# set comprehension
start = int(input("\nEnter start of range: "))
end = int(input("Enter end of range: "))
squares = {x ** 2 for x in range(start, end + 1) if x % 2 == 0}
print("Squares of even numbers:", squares)
