# simple inheritance
class Employees:
    inTime = "10am"
    outTime = "6pm"

class Teacher(Employees):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_info(self):
        print(f"{self.name} is come at{self.inTime} and went back by {self.outTime} and he teach {self.subject}")

t1 = Teacher("sahil","Math")
t1.get_info()
print(t1.name,t1.subject,t1.inTime,t1.outTime)


#super() function
class Animal:
    def __init__(self,wild):
        self.wild = wild

class Tiger(Animal):
    def __init__(self,color, wild):
        super().__init__(wild)
        #without super method
        # Animal.__init__(self,wild)
        self.color = color

t1 = Tiger("yellow",True)
print(t1.color,t1.wild)

# another example
class Animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"Name of Animal: {self.name}")

class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread

    def details(self):
        print(f"The {self.name} is a {self.bread}")

d1 = Dog("rocky","lab")
d1.info()
d1.details()

# type of inherotance
# 1) single inheritance

class Employees:
    company_name = "VIT Institude"

class Employees_details(Employees):
    def __init__(self,name, age, salary):
        # super().__init__(self.company_name)
        # Employees.__init__(self.company_name)
        self.name = name
        self.age = age
        self.salary = salary

    def get_info(self):
        print(f"Employee of {self.company_name},is {self.age} years old and his salary is:{self.salary}")

e1 = Employees_details("amit",33, 20_000)
e1.get_info()

