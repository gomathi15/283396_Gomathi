from Management import Employee, Department, save_to_json, load_from_json

# Sample data strings (Employee data)
data_strings = [
    "Alice,30,Female,E101,HR,48000",
    "Bob,28,Male,E102,IT,55000",
    "Charlie,35,Male,E103,HR,60000",
    "Diana,26,Female,E104,IT,47000",
    "Evan,40,Male,E105,Finance,53000"
]

# Create Employee objects from the data strings
employees = [Employee.from_string(s) for s in data_strings]

# Create Departments and assign employees
departments = {}
for emp in employees:
    if emp.department not in departments: 
        departments[emp.department] = Department(emp.department)
    departments[emp.department].add_employee(emp)

# Print the bonus policy
Employee.bonus_policy()

# Print Employee Details
print('-'*100)
print("\nEmployee Details:")
for emp in employees:
    print(emp.get_details())
print('-'*100)

# Print Department Average Salaries
print("\nAverage Salaries by Department:")
print('-'*100)
for dept_name, dept in departments.items():
    print(f"{dept_name}: ₹{dept.get_average_salary():.2f}")
print('-'*100)

#Print Average salary of employees 
def get_average_salary_of_employees(employees):
    total_salary = sum(emp.salary for emp in employees)
    return total_salary / len(employees) if employees else 0


# Calculate and print the average salary of all employees
average_salary = get_average_salary_of_employees(employees)
print(f"\nAverage Salary of All Employees: ₹{average_salary:.2f}")
print('-'*100)

# Save Employee Data to JSON file
save_to_json(employees)

# Load Employee Data from JSON file
print("\n📂 Loaded Data from JSON:")
loaded_emps = load_from_json()  # Load data from JSON and create Employee objects
for emp in loaded_emps:
    print(emp.get_details())
