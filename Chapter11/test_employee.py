import os
import unittest
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
from Classes.employee import Employee

class TestEmployee(unittest.TestCase):
    """tests for class Employee.py"""

    def setUp(self):
        firstName = "Renato"
        lastName = "Regalado"
        annualSalary = 70000

        self.my_emp = Employee(firstName,lastName,annualSalary)
    
    def test_give_custom_Raise(self):
        """test that the employee gets a raise"""
        self.raiseAmount = 10000
        self.my_emp.giveRaise(self.raiseAmount)
        self.assertEqual(self.my_emp.annualSalary, 80000)

    def test_give_default_Raise(self):
        """test that the employee gets a raise"""
        self.my_emp.giveRaise()
        self.assertEqual(self.my_emp.annualSalary, 75000)


if __name__ == '__main__':
    unittest.main()