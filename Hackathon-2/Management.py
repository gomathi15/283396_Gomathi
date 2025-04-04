import json

# Creating class for the employee name, age, gender
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    

#Creating class for the employee ID, Department, Salary
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        
        return f"{super().get_details()}, Employee ID: {self.emp_id}, Department: {self.department}, Salary: {self.salary}"

    def is_eligible_for_bonus(self):
    
        return self.salary < 50000

    @classmethod
    def from_string(cls, data_string):
        
        data = data_string.split(',')
        return cls(data[0], int(data[1]), data[2], data[3], data[4], float(data[5]))

    @staticmethod
    def bonus_policy():
        
        print('\n')
        print("Bonus Policy - Employees earning less than 50,000 are eligible for a bonus.")


#creating class for the department to an employee
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        
        self.employees.append(employee)

    def get_average_salary(self):
        
        if self.employees:
            total_salary = sum(emp.salary for emp in self.employees)
            return total_salary / len(self.employees)
        return 0  

    def get_all_employees(self):
        
        return [emp.get_details() for emp in self.employees]


 #Data persistence (saving the data to the json and loading the json file)
 # import json

# Function to save all employee data to a JSON file
def save_to_json(employees, filename="employees.json"):
    with open(filename, 'w') as file:
        # Convert employee objects to dictionaries (to make them JSON serializable)
        employees_data = [emp.__dict__ for emp in employees]
        json.dump(employees_data, file, indent=4)

# Function to load employee data to Department
def load_from_json(filename="employees.json"):
    with open(filename, 'r') as file:
        # Load the employee data from JSON file
        employees_data = json.load(file)
        employees = []
        
        for data in employees_data:
            # Recreate Employee objects from the loaded data
            emp = Employee(data['name'], data['age'], data['gender'], data['emp_id'], data['department'], data['salary'])
            employees.append(emp)
        
        return employees
   
