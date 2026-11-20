"""student.results - module for student results."""


def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks, max_per_subject=100):
    return sum(marks) / (len(marks) * max_per_subject) * 100


def get_grade(percentage):
    if percentage >= 75:
        return "Distinction"
    if percentage >= 60:
        return "First Class"
    if percentage >= 40:
        return "Pass"
    return "Fail"


def display_result(name, marks):
    total = calculate_total(marks)
    pct = calculate_percentage(marks)
    print("----- Student Result -----")
    print(f"Name       : {name}")
    print(f"Total      : {total}")
    print(f"Percentage : {pct:.2f}%")
    print(f"Grade      : {get_grade(pct)}")
