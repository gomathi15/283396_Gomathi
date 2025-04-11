
from employee_manager import Employee_data
from storage import Storage

def display_employee(emp):
    print("\nEmployee Details:")
    print(f"ID: {emp.id}")
    print(f"Name: {emp.name}")
    print(f"Department: {emp.department}")
    print(f"Designation: {emp.designation}")
    print(f"Gross Salary: {emp.gross_salary}")
    print(f"Tax: {emp.tax}")
    print(f"Bonus: {emp.bonus}")
    print(f"Net Salary: {emp.net_salary}")
    print("-" * 30)

def main():
    manager = Employee_data()
    storage = Storage()

    # Load data from file
    loaded_employees = storage.load()
    manager.load_tasks([emp.to_dict() for emp in loaded_employees])

    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Name: ")
            department = input("Department: ")
            designation = input("Designation: ")
            gross_salary = float(input("Gross Salary: "))
            tax = float(input("Tax: "))
            bonus = float(input("Bonus: "))

            net_salary = gross_salary - tax + bonus
            emp = manager.add_employee(name, department, designation, gross_salary, bonus, tax, net_salary)
            print("Employee added successfully!")
            display_employee(emp)

        elif choice == "2":
            all_emps = manager.get_all_employees()
            if not all_emps:
                print("No employees found.")
            else:
                for emp in all_emps:
                    display_employee(emp)

        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            emp = manager.search_employee(emp_id)
            if emp:
                display_employee(emp)

        elif choice == "4":
            emp_id = input("Enter Employee ID to delete: ")
            if manager.delete_employee(emp_id):
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")

        elif choice == "5":
            # Save before exiting
            storage.save(manager.get_all_employees())
            print("Data saved. Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
