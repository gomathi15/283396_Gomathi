import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee_manager import Employee_data
 
class TestEmpManager(unittest.TestCase):
    def setUp(self):
        self.manager = Employee_data(file="test_emp.pkl")
 
    def test_add_employee(self):
        emp = self.manager.add_employee("vela", "semicon", "t1", 400000, 10000, 3000)
        self.assertEqual(emp.name, "vela")
        self.assertEqual(len(self.manager.employees), 1)
 
if __name__ == "__main__":
    unittest.main()