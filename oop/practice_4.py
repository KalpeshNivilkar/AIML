# product store 

class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1  # class attribute does not take self they want class name

    def get_info(self):
        print(f"the price of {self.name} is {self.price}.")
    @classmethod
    def count_product(cls):
        print(f"the total product are {cls.count}")

    @staticmethod
    def cal_discount(price, discount):
        print(f"the final discount is {price - (price * discount / 100) }")


p1 = Product("laptop", 20000)  
p2 = Product("TV", 10000)


p1.cal_discount(p1.price,10)




# craete a bank account  class with attributes account_number, owner_name, and balance add methods to deposite withdraw and check balance

'''class Bank_account:
    def __init__(self, account_number, owner_name, balance ):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance


    def deposite(self,amount):
        self.balance += amount
        print(f"{amount} is deposite successfully!")

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance -= amount
            print(f"withdraw Rs.{amount} is successful!")

    def check_balance(self):
        print(f"current balance of {self.owner_name} is :{self.balance}")




a1 = Bank_account(101,"kalpesh",20000)
a2 = Bank_account(102,"aditya",30000)
a1.deposite(5000)
a2.withdraw(5000)
a1.check_balance()'''
 


        

