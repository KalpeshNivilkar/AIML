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