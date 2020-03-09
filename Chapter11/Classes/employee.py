class Employee: 
    """create an Employee Class"""
    def __init__(self, firstName, lastName, annualSalary):
        self.firstName = firstName
        self.lastName = lastName
        self.annualSalary = annualSalary
    
    def describeEmployee(self):
        print(f"First name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Annual Salary: ${self.annualSalary}")

    def giveRaise(self, raiseAmount = 5000):
        self.annualSalary += raiseAmount
        print(f"{self.firstName}'s salary has increased by {raiseAmount}'")
        print(f"{self.firstName}'s salary is now {self.annualSalary}'")


# myEmployee = Employee("Renato","Regalado",70000)
# myEmployee.describeEmployee()
# myEmployee.giveRaise(10000)
# print(myEmployee.annualSalary)