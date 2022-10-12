"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from abc import ABC, abstractclassmethod

class Contract():

    def __init__(self):
        pass

    def getSalary(self):
        pass

    def __str__(self):
        pass

class SalaryContract(Contract):
    def __init__(self, salary):
        super().__init__()
        self.salary = salary
    
    def getSalary(self):
        return self.salary

    def __str__(self):
        return f"works on a monthly salary of {self.salary}"

class HourlyContract(Contract):
    def __init__(self, hoursWorked, hourlyWage):
        super().__init__()
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked

    def getSalary(self):
        return self.hoursWorked * self.hourlyWage

    def __str__(self):
        return f"works on a contract of {self.hoursWorked} at {self.hourlyWage}/hour"

class Commission():
    def __init__(self):
        pass

    def getCommission(self):
        pass
    
    def __str__(self):
        pass

class NoCommission(Commission):
    def __init__(self):
        super().__init__()
        self.commission = 0

    def getCommission(self):
        return 0

    def __str__(self):
        return ""

class BonusCommission(Commission):
    def __init__(self, commission):
        super().__init__()
        self.commission = commission

    def getCommission(self):
        return self.commission

    def __str__(self):
        return f" and receives a bonus commission of {self.commission}"

class ContractCommission(Commission):
    def __init__(self, contracts, commission):
        super().__init__()
        self.contracts = contracts
        self.commission = commission

    def getCommission(self):
        return self.contracts * self.commission

    def __str__(self):
        return f" and receives a commission for {self.contracts} contract(s) at {self.commission}/contract"



class Employee():
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission
        self.totalPay = contract.getSalary() + commission.getCommission()


    def __str__(self):
        return f"{self.name} " + self.contract.__str__() + self.commission.__str__() + f".  Their total pay is {self.totalPay}."
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000), NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(100, 25), NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(120, 30), BonusCommission(600))

print(billie.__str__())
print(charlie.__str__())
print(renee.__str__())
print(jan.__str__())
print(robbie.__str__())
print(ariel.__str__())