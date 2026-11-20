"""Unit 4 - Q2: File Handling - Read, Write and Append (student.txt)"""

# 1-2. Create/open in write mode and write student details
f = open("student.txt", "w")
n = int(input("How many students to enter? "))
for i in range(n):
    name = input(f"Student {i + 1} name: ")
    roll = input("Roll no: ")
    course = input("Course: ")
    f.write(f"{roll},{name},{course}\n")
f.close()
print("Records written to student.txt")

# 3. Read complete contents
f = open("student.txt", "r")
print("\n--- Complete file contents ---")
print(f.read())
f.close()

# 4. Append more records
f = open("student.txt", "a")
m = int(input("How many more students to append? "))
for i in range(m):
    name = input(f"Student {i + 1} name: ")
    roll = input("Roll no: ")
    course = input("Course: ")
    f.write(f"{roll},{name},{course}\n")
f.close()

# 5. Read line by line
f = open("student.txt", "r")
print("\n--- Reading line by line ---")
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()
f.close()

# 6. Display all lines with readlines()
f = open("student.txt", "r")
print("\n--- Using readlines() ---")
for number, line in enumerate(f.readlines(), start=1):
    print(f"Line {number}: {line.strip()}")

# 7. Close file
f.close()
print("\nFile closed:", f.closed)
