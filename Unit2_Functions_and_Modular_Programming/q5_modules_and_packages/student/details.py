"""student.details - module for student details."""


def get_details(name, roll_no, course):
    return {"name": name, "roll_no": roll_no, "course": course}


def display_details(details):
    print("----- Student Details -----")
    print(f"Name   : {details['name']}")
    print(f"Roll No: {details['roll_no']}")
    print(f"Course : {details['course']}")
