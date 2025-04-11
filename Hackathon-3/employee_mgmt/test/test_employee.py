import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee import Employee
 
class TestEmp(unittest.TestCase):
    def test_employee_creation(self):
        emp = Employee("Gomathi", "semicon", "Tester", 500000, 5000, 2000)
        self.assertEqual(emp.name, "Gomathi")
        self.assertEqual(emp.department, "semicon")
        self.assertEqual(emp.designation, "Tester")
        self.assertEqual(emp.net_salary, 470000)
 
if __name__ == "__main__":
    unittest.main()
 