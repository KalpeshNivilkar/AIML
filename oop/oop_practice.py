# Q1

'''print("------Welcome To Bank of Maharashtra_------")
class BankAccount:

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def get_info(self):
        print(f"Acc Number : {self.account_number}, Holder Name: {self.owner_name}, Balance:{self.balance}")

    def deposite(self, amount):
        self.amount = amount

        if amount > 0:
            self.balance += amount
            print(f"{self.amount} Amount added sucseefully...")
            print(f"Current balance is: {self.balance}")
        else:
            print("Enter valid amount!")

    def withdraw(self, amount):
        self.amount = amount

        if amount > self.balance:
            print(f"You cannot withdraw {amount}")
        else:
            self.balance -= amount
            print(f"{amount} withdraw successfully...")
            print(f"Current balance is: {self.balance}")

    def check_balance(self):
        print(f"Current blance is: {self.balance}")

acc1 = BankAccount(101,"kalpesh",20_000)
acc1.get_info()
acc1.deposite(10_000)
acc1.deposite(0)
acc1.withdraw(5000)
acc1.withdraw(26000)
acc1.check_balance()'''

# Q2

'''class Book:
    count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author  
        self.list_of_review = []
        
    def get_info(self):
        print(f"The name of Book : {self.title}, The author : {self.author}, list_of_review :{self.list_of_review}") 

    def add_review(self, review):
        self.review = review

        self.list_of_review.append(review)
        Book.count += 1
        print(f"your review is added successfully...")

    @classmethod
    def count_review(cls):
       print(f"Total count of review : {cls.count}")

    def display_all_review(self):
        print(f"All reviews : {self.list_of_review}")

b1 = Book("Rich Dad Poor Dad", "Robert T. Kiyoski")
b1.get_info()
b1.add_review("so deep thought...")
b1.count_review()
b1.add_review("so deep thought...")
b1.count_review()
b1.display_all_review()'''

# Q3

'''class Student:
    def __init__(self,name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_info(self):
        print(f"Name of Student: {self.__name}, Roll no: {self.__roll_no}, Marks: {self.__marks}")

    def set_marks(self, marks):
       
        if marks < 0 or marks > 100:
            print(f"{marks}: Negative marks not allow...")
        else:
            self.__marks = marks

    def set_roll_no(self, roll_no):
        
        if roll_no < 0 or roll_no > 100:
            print(f"{roll_no} is not found...")
        else:
            self.__roll_no = roll_no
        

    def set_name(self, name):
        
        if name == "":
            print(f"Student name is not found!")
        else:
            self.__name = name
        

s1 = Student("kalpesh", 450, 100)
s1.get_info()
s1.set_marks(23)
s1.set_name("avina")
s1.set_roll_no(30)
s1.get_info()
'''

# Q4
"""class Shape:
    def area(self):
        print("Area of shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print("The area of circle is", 3.14 * self.radius *self.radius)

class Rectangular(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangular:", self.length * self.width)

c = Circle(5)
r = Rectangular(10,10)      

c.area()
r.area()"""

# Q5

"""class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        print(f"Name of Brand: {self.brand} Name of Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def car_info(self):
        print(f"Brand: {self.brand}, model: {self.model}, seats: {self.seats} ")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc ):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def bike_info(self):
        print(f"Brand: {self.brand},model: {self.model}, engine_cc:{self.engine_cc} ")

b1 = Bike("honda","bike_model",125)
b1.bike_info()
c1 = Car("suzuki", "new", 4)
c1.car_info()
"""
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

    
    






