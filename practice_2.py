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

def sum_of_digit(num):
    summ = 0
    while num > 0:
        digit = num % 10
        summ += digit
        num = num // 10
    return summ
num = 312
print(sum_of_digit(num))


  
    
       
        

    