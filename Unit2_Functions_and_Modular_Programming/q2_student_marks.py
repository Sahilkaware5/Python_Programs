"""Unit 2 - Q2: Variable-Length Arguments and Return Statement
Total, average and highest marks using *args and **kwargs.
"""


def calculate_result(name, *marks, **info):
    """*marks takes marks of any number of subjects,
    **info takes extra details (roll_no, class, ...).
    Returns total, average and highest marks."""
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    return total, average, highest


if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    student_class = input("Enter class: ")
    n = int(input("Enter number of subjects: "))

    subjects, marks = [], []
    for i in range(n):
        subjects.append(input(f"Enter name of subject {i + 1}: "))
        marks.append(float(input(f"Enter marks in {subjects[i]}: ")))

    total, average, highest = calculate_result(
        name, *marks, roll_no=roll_no, student_class=student_class
    )
    top_subject = subjects[marks.index(highest)]

    print("\n" + "=" * 40)
    print(f"{'STUDENT RESULT':^40}")
    print("=" * 40)
    print(f"Name       : {name}")
    print(f"Roll No    : {roll_no}")
    print(f"Class      : {student_class}")
    print("-" * 40)
    for s, m in zip(subjects, marks):
        print(f"{s:<20}{m:>10.2f}")
    print("-" * 40)
    print(f"{'Total Marks':<20}{total:>10.2f}")
    print(f"{'Average Marks':<20}{average:>10.2f}")
    print(f"{'Highest Marks':<20}{highest:>10.2f} ({top_subject})")
    print("=" * 40)
