# Employee Salary Analysis

employees = [
    {"id": "E101", "department": "IT", "salary": 45000},
    {"id": "E102", "department": "IT", "salary": 60000},
    {"id": "E103", "department": "HR", "salary": 40000},
    {"id": "E104", "department": "HR", "salary": 55000}
]

# Store salaries department-wise
departments = {}

for employee in employees:
    department = employee["department"]
    salary = employee["salary"]

    if department not in departments:
        departments[department] = []

    departments[department].append(salary)

# Calculate average salary and find employees above average
for department, salaries in departments.items():

    average_salary = sum(salaries) / len(salaries)

    print(f"{department} Average Salary: {average_salary:.0f}")

    for employee in employees:
        if employee["department"] == department and employee["salary"] > average_salary:
            print(f"Employee above {department} average: {employee['id']}")

    print()
