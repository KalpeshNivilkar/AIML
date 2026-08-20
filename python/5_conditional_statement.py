# grade stedents based on a marks
'''marks = int(input("enter the marks: "))
if marks >= 75 and marks <= 100:
    print("grade A")
elif marks >= 55 and marks <= 74:
    print("grade B")
elif marks >= 35 and marks <= 54:
    print("grade C")
else:
    print("fail")'''

# WAP to check if a number entered by the user is odd or even.
'''num = int(input("enter any number: "))
def is_num_even_odd(num):
    if num % 2 == 0:
        print("The",num,"is even")
    else:
        print("the",num,"is odd")
is_num_even_odd(num)'''

# WAP to find the greatest of 3 numbers entered by the user.
'''num1 = int(input("enter  num 1:"))
num2 = int(input("enter  num 2:"))
num3 = int(input("enter  num 3:"))

if num1 > num2 and num1 > num3:
    print(num1,"is greater")
elif num2 > num1 and num2 > num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")'''

# WAP to c

# A
# heck
# p
# if a number is a multiple of 7 or not.

'''num = int(input("enter the number: "))
if num % 7 == 0:
    print(num,"is divisible by 7")
else:
    print(num,"is not divisible by 7")'''



'''age = int(input("enter your age:"))

if age <= 13:
    print("you are child")
elif age > 13 and age < 18:
    print("you are teenager")
elif age >= 18:
    print("you are adult")'''

'''username = input("enter ypur username: ")
password = input("enter your password: ")

user_name = "admin"
user_pass ="123"

if username == user_name and password == user_pass:
    print("login successful...")
else:
    print("Invalid Credientials.. try again..")'''

# print odd even num

'''n = int(input("enter any number: "))

if n % 2 == 0:
    print(n,"is even number")
else:
    print(n,"is odd number")'''


# multiplication table of any n 
'''n = int(input("enter ay number:"))
i = 1
while i <= 10:
    print(n * i)
    i += 1'''


# break 
i = 1
while i <= 10:
    if i % 6 == 0:
        break
    print(i)
    i += 1
print("os loop")
   