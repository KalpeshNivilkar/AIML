'''there is two kind of attributes
1. class attribute
2 instance attributes'''

class Student:
    college_name = "MIT" #class attribute

    def __init__(self, name, age):
        self.name = name  #instance attribute
        self.age = age    #instance attribute

std = Student("kalpesh", 23)

print(std.name, std.age, std.college_name)                # print using object/ instance
print(Student.college_name)                               # print using class name & it does not take any instance attribute



# lets if both have same attributes

class Teacher:
    college_name = "VIT"
    subject = "python"      # same attribute

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject    # same attribute

tec = Teacher("amit",30, "java")
print(tec.name, tec.age, tec.college_name,tec.subject)



