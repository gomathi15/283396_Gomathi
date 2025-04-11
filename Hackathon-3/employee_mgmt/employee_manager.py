from employee import Employee
 
class Employee_data(object):
    def __init__(self):
        self.data = []
 
    # Add new employee
    def add_employee(self, name,department,designation, gross_salary,net_salary, bonus, tax):
        emp = Employee(name,department,designation,gross_salary,net_salary, bonus, tax )
        self.data.append(emp)
        return emp
 
    # View all employees
    def get_all_employees(self):
        return self.data
 
    # Search employee by ID
    def search_employee(self, emp_id):
        for emp in self.data:
            if emp.id == emp_id:
                return emp
        print(" No employee found with that ID.")
        return None
 
    # Delete a employee
    def delete_employee(self, emp_id):
        for emp in self.data:
            if emp.id == emp_id:
                self.data.remove(emp)
                return True
        return False
 
    # Load employees from a list of dictionaries
    def load_tasks(self, employee_dicts):
        self.data = [Employee.from_dict(td) for td in employee_dicts]
 
    # Convert employees to list of dictionaries
    def to_dict_list(self):
        return [emp.to_dict() for emp in self.data]