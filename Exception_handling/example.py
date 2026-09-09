'''# first example
try:
    n = int(input("enter the value of n:"))
    ans = 10/ n
except ZeroDivisionError:
    print("divide by zero not allowed...")

except ValueError:
    print("enter wrong input...")

else:
    print(f"the ans is: {ans}")

finally:
    print("program is end...")


    '''

# Take two numbers from the user.
# Divide the first number by the second.
# Handle ValueError if the user enters something that isn't a number.
# Handle ZeroDivisionError if the second number is 0.
# Print "Division successful" when there is no error.

'''try:
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    num3 = num1 / num2

except ValueError:
    print("you entered invalid value...")

except ZeroDivisionError:
    print("Divided by zero is not possible...")

else:
    print(f"num3 = {num3}")'''


# Write a program that asks the user for a filename and tries to open it.

# Requirements:

# Ask the user for a filename.
# Try to open the file in "r" mode.
# Handle FileNotFoundError.
# If the file exists, print its contents.
# Use finally to print:
# Program execution completed.
import json

try:
    file_name = input("Enter a file name: ")
    with open(file_name, "r") as f:
        data = json.load(f)
    print(data)

except FileNotFoundError:
    print("you have enter wrong file name")

finally:
    print("program executed successfully...")