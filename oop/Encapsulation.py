# access modifiers 
# 1) public

class Bank_acc:
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance   #public

    def get_details(self):
        print(f"{self.name} has {self.balance} $ balance...")

acc1 = Bank_acc("kalpesh", 20_000)
acc1.get_details()

# 2) protected

class Student:
    def __init__(self, name,acc_details):
        self.name = name   #public
        self._acc_details = acc_details   #protected 

        print(f"{name} has acc_details: {acc_details}")

s1 = Student("kalpesh","Yes")
print(s1.name,s1._acc_details)


# 3) private

class Teacher:
    def __init__(self, name, salary):
        self.name = name #public
        self.__salary = salary #private

    def show_data(self):
        print(f"{self.name} has {self.__salary} salary...") #output: Sahil has 20000 salary...

t1 = Teacher("Sahil",20_000)
t1.show_data()
print(t1.name, t1.__salary) #output: it throws an error
