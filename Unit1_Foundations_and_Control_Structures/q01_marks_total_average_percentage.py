"""Q1: Total, average and percentage of marks in five subjects."""

marks = []
for i in range(1, 6):
    marks.append(float(input(f"Enter marks of subject {i} (out of 100): ")))

total = sum(marks)
average = total / 5
percentage = total / 500 * 100

print(f"\nTotal marks : {total}")
print(f"Average     : {average:.2f}")
print(f"Percentage  : {percentage:.2f}%")
