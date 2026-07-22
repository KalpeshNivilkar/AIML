# craete a bank account  class with attributes account_number, owner_name, and balance add methods to deposite withdraw and check balance

class Bank_account:
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
a1.check_balance()

