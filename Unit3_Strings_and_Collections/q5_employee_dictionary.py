"""Unit 3 - Q5: Dictionaries, Dictionary Comprehension and Nested Collections"""

# Nested dictionary: employee ID -> employee details
employees = {
    101: {"name": "Amit Sharma", "department": "IT", "salary": 55000},
    102: {"name": "Neha Patil", "department": "HR", "salary": 42000},
    103: {"name": "Rahul Deshmukh", "department": "Finance", "salary": 61000},
}


def show_all():
    print(f"{'ID':<6}{'Name':<18}{'Department':<14}{'Salary':>8}")
    for emp_id, d in employees.items():
        print(f"{emp_id:<6}{d['name']:<18}{d['department']:<14}{d['salary']:>8}")


print("=== Initial employees ===")
show_all()

# Add
employees[104] = {"name": "Sneha Kulkarni", "department": "IT", "salary": 48000}
print("\n=== After adding 104 ===")
show_all()

# Update
employees[102]["salary"] = 46000
employees[101].update({"department": "Development"})
print("\n=== After updating 102 salary and 101 department ===")
show_all()

# Delete
del employees[103]
removed = employees.pop(104)
print(f"\n=== After deleting 103 and pop(104) -> {removed['name']} ===")
show_all()

# keys, values, items
print("\nKeys  :", list(employees.keys()))
print("Values:", list(employees.values()))
print("Items :", list(employees.items()))

# Search
emp_id = int(input("\nEnter employee ID to search: "))
if emp_id in employees:
    print("Employee found:", employees.get(emp_id))
else:
    print("Employee not found.")

# Dictionary comprehension
limit = int(input("\nEnter salary limit: "))
high = {i: d for i, d in employees.items() if d["salary"] > limit}
print(f"Employees earning above {limit}:", high)
