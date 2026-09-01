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

class Book:
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
b1.display_all_review()

