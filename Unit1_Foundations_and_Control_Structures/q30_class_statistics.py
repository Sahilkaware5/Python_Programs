"""Q30: Class statistics for N students (marks out of 100, pass mark = 40)."""

n = int(input("Enter number of students: "))

marks = []
for i in range(1, n + 1):
    marks.append(float(input(f"Enter marks of student {i}: ")))

average = sum(marks) / n
highest = max(marks)
lowest = min(marks)
passed = sum(1 for m in marks if m >= 40)
failed = n - passed
above_75 = sum(1 for m in marks if m > 75)

print(f"\nClass average         : {average:.2f}")
print(f"Highest marks         : {highest}")
print(f"Lowest marks          : {lowest}")
print(f"Passed students       : {passed}")
print(f"Failed students       : {failed}")
print(f"Students above 75%    : {above_75}")
