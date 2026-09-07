# first example
try:
    n = int(input("enter the value of n:"))
    ans = 10/ n
except ZeroDivisionError:
    print("divide by zero not allowed...")

except ValueError:
    print("enter wrong input...")

else:
    print(f"the ans is: {ans}")

