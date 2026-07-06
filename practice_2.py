'''Q1
salary
. Write a program that takes  as input. Using conditional statements, 
calculate the  
final tax rate
based on these rules:
• 
If salary < 30,000 → 5%
• 
If salary is 30,000–70,000 → 15%
• 
If salary > 70,000 → 25%'''

'''salary = int(input("enter your salary: "))
if salary <= 30000:
    tax = (salary * 5)/100
elif salary > 30000 and salary <= 70000:
    tax = (salary * 15)/100
else:
    tax = (salary * 25)/100

print("Pay Tax $",tax, "on the salary of:",salary)'''

# Q2.
# a b
# Write a function that takes two integers  and  and prints all even 
# numbers between them (inclusive).

'''def even_num(a,b):
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i)
a = int(input("enter the starting number:"))
b = int(input("enter the ending number: "))
even_num(a,b)'''

# Q3
# . Write a function that prints the  
# n = 312
# digits
# n
# of a number, . 
# For eg:  , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [ 
# Hint- The right most digit of a number N is N%10. 
# And to remove the right most digit from a number, we can do N = N / 10.]
    
'''def extract_digit(nums):
    while nums > 0:
        digit = nums% 10
        print(digit)
        nums = nums // 10
nums = 312
extract_digit(nums)'''

# Q4
# . Write a function to return the  

# count
# n
# the number of digits in a number, .

'''def count_num(n):
    count = 0
    while n > 0:
        digit =  n % 10
        count += 1
        n = n // 10
    return count
n = 312
print(count_num(n))'''


# write a function to return sum  of digit

'''def sum_of_digit(num):
    summ = 0
    while num > 0:
        digit = num % 10
        summ += digit
        num = num // 10
    return summ
num = 312
print(sum_of_digit(num))'''

# Write a program to print all numbers from 1 to 100 that are divisible by both 3 
# and 5.

'''def divisible_num():
    for i in range(1,100):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
divisible_num()'''


#  Design a program to continuously input a number  from user & print if it is 
# positive or negative until the user enters “Quit”.

'''while True:
    user_input = input("enter a number or Quit: ")
    if user_input == "Quit":
        print("program end...")
        break
    num = int(user_input)
    if num > 0:
        print(num,"is positive.")
    else:
        print(num,"is negative")
'''
   
        
# Letʼs create a Simple  
# Calculator
# calculator(a, b, operation)
# that performs arithmetic operations. Create 
# a function  that performs addition, subtraction, 
# multiplication, or division based on the  parameter.  
# operation
# [ 
# operation ‘+’ ‘-’ '*’ ‘/’
# parameter can have values ,  ,  & .


'''def calculator(a, b, operation):
    if operation == '+':
        print("addition of a and b is", a+b)
    elif operation == '-':
        print("subtraction of a and b is", a-b)
    elif operation == '*':
        print("mul of a and b is", a*b)
    elif operation == '/':
        if b == 0:
            print("divisible by zero is not allow...") 
        else:
            print("div of a and b is", a/b)
    else:
        print("Invalid Operation...")
        print("choose +, -, *, /")

a = int(input("enter the num1 : "))
b = int(input("enter the num2 :"))
operation = input("enter the operand to perform the operation,(ig: +, -, *, /):")
calculator(a,b,operation)'''

#  Write a function  
# prime(n)
# True n
# that returns  if  is a prime number and 
# False
# [ 
# Hint- 
# otherwise, using a loop.
# non-Prime
# n
# 2
# 1. We only check prime for 2 or numbers greater than 2.  is the smallest 
# prime number.
# 2. A  number, , will always get divided by atleast one number in 
# range [2, n-1].
# 9 9
# Eg - For number  weʼll check in range (2, 8) & itʼll get divided by 3. So  is 
# non-prime & weʼll return false for it.
# For number  weʼll check in range (2, 6) & it wonʼt get divided by any. So 
# is prime & weʼll return true for it. ]

# def is_prime(n):
#     for i in range(2,n-1):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("enter the number:"))   
# print(is_prime(n))


# Letʼs create a “
# Number Guessing Game
# ”.  Given a secret number (already 
# decided by you), write a program that asks the user to guess it and prints:
# •
 
# •
 
# •
 
# "Too high"
# "Too low"
# if the guess is above the number
# if the guess is below
# "Correct!"
# if the guess matche

def number_gasing_game():
    secret_num = 100
    while True:
        n = int(input("enter the number:"))

        if n == 100:
            print("you are won...")
            break
        elif n >= secret_num:
            print("too high..")
            # continue
        elif n <= secret_num:
            print("too low...")
            # continue
        else:
            print("Invalid choice!")
            print("enter the number digit, ig:23,119")

number_gasing_game()
       
        

    