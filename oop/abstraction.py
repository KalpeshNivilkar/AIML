'''from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("roar")

class cow(Animal):
    def make_sound(self):
        print("moo")

l1 = cow()
l1.make_sound()

l2 = Lion()
l2.make_sound()'''

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("salary: 20_000")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("salary: 50_000")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("salary: 30_000")

c1 = ContractEmployee()
c1.calculate_salary()

    
    






