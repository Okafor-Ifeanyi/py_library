from urllib import request
from eg import days

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property    
    def email(self):  
        return self.first + '.' + self.last + '@gmail.com'

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            num = day.weekday()
        return days(num)

    def monthly_schedule(self, month):
        response = request.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"


# emp_1 = Employee('Prog', "BIO", 5000)
# emp_2 = Employee('Dexter', "Oil", 6000)

# Employee.set_raise_amt(1.06)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# import datetime

# my_date = datetime.date(2019, 9, 8)

# print(Employee.is_workday(my_date))