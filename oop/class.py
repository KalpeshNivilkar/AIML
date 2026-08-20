'''# design instance, class and static methods

class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"product name : {self.name} and the price : Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"count of product is: {cls.count}")

    @staticmethod
    def cal_discount(price, percentage):
        print(f"the discount on product is: {price - (price * percentage/ 100)}")

p1 = Product("besan",100)
p2 = Product("phone",20000)
p1.get_info()
p2.get_info()
p1.get_count()
p1.cal_discount(p1.price,20)'''


class Student:
    college_name = "ABC"
    year = "4th"
    subject = "python"

for std in range(30):
    std = Student()
    print(std.college_name, std.year, std.subject)