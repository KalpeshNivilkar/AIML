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


# another example of single inheritense

class Employees:
    def work(self):
        print("employees are working..")

class Teacher(Employees):
    def work_in_office(self):
        print("they are working out in the office..")

t1 = Teacher()
t1.work()
t1.work_in_office()

# multiple inheritance
class Father:
    def __init__(self,f_name):
        self.f_name = f_name
    def f_info(self):
        print(f"name of father is : {self.f_name}")

class Mother:
    def __init__(self, m_name):
        self.m_name = m_name
    def m_info(self):
        print(f"name of mother is : {self.m_name}")

class Son(Mother,Father):
    def __init__(self, f_name,m_name, s_name):
        super().__init__(m_name)
        Father.__init__(self, f_name)
        self.s_name = s_name

    def s_info(self):
        print(f"name of father is {self.f_name}")
        print(f"name of mother is :{self.m_name}")
        print(f"name of son is {self.s_name}")

s1 = Son("subhash","kashi","kalpesh")
s1.f_info()
s1.m_info()
s1.s_info()
        


# multilevel inheritanse

'''class GrandFather:
    def __init__(self, gf_name, gf_age):
        self.gf_name = gf_name
        self.gf_age = gf_age

    def get_gf_info(self):
        print(f"Grandfather name is {self.gf_name} and his age : {self.gf_age} years...")

class GrandMother(GrandFather):
    def __init__(self, gf_name, gf_age, gm_name, gm_age):
        super().__init__(gf_name, gf_age)
        self.gm_name = gm_name
        self.gm_age = gm_age

    def get_gm_info(self):
        print(f"grandfather name is {self.gf_name} and grandmother name is {self.gm_name}")

class Father(GrandMother):
    def __init__(self, gf_name, gf_age, gm_name, gm_age,father_name):
        super().__init__(gf_name, gf_age, gm_name, gm_age)
        self.father_name = father_name

    def get_father_info(self):
        print(f"name of grandfather is {self.gf_name}, name of grandmother is {self.gm_name} and father name is {self.father_name}")

f1 = Father("ganapat",70,"sita",65,"subhash")
f1.get_gf_info()
f1.get_gm_info()
f1.get_father_info()'''
    
