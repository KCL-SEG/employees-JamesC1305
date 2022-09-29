"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, wage, hours=0, commissionValue=0, contractsLanded=0):
        self.name = name
        self.contractType = contractType
        self.wage = wage
        self.hours = hours
        self.commissionValue = commissionValue
        self.contractsLanded = contractsLanded


    def get_pay(self):
        self.pay = 0
        if self.contractType == "contract":
            self.pay = self.wage * self.hours
            if self.commissionValue:
                if self.contractsLanded:   
                    self.pay = self.contractsLanded*self.commissionValue + self.wage
                else:
                    self.pay = self.commissionValue + self.wage
        else:
                if self.commissionValue:        
                    if self.contractsLanded:
                        self.pay = self.contractsLanded*self.commissionValue + self.wage
                    else:
                        self.pay = self.commissionValue + self.wage
        return self.pay


    def __str__(self):
        if self.contractType == "salary":
            if self.commissionValue:
                if self.contractsLanded:
                    return f"{self.name} works on a monthly salary of {self.wage} and receives a commission for {self.contractsLanded} at {self.commissionValue}/contract. Their total pay is {self.get_pay()}"
                else:
                    return f"{self.name} works on a monthly salary of {self.wage} and receives a bonus commission of {self.commissionValue}. Their total pay is {self.get_pay()}"
            else:
                return f"{self.name} works on a monthly salary of {self.wage}. Their total pay is {self.get_pay()}"
        else:
            if self.commissionValue:
                if self.contractsLanded:
                    return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.contractsLanded} at {self.commissionValue}/contract. Their total pay is {self.get_pay()}"
                else:
                    return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.commissionValue}. Their total pay is {self.get_pay()}"
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "contract", 25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', 3000, hours=0, contractsLanded=4, commissionValue=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "contract", 25, hours=150, contractsLanded=3, commissionValue=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", 2000, commissionValue=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "contract", 30, hours=120, commissionValue=600)

