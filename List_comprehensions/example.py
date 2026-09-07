# example no 1 
nums = [1,2,3,4,5]

new_nums = [el * el for el in nums if el % 2 != 0]
print(nums)

# example no 2

fruits = ["banana","apple", "chiku"]

new_fruits = [val for val in fruits if "a" in val]
print(new_fruits)

# example no 3
numbers = [1, 2, 3, 4, 5]
square_of_nums = [i * i for i in numbers]
print(square_of_nums)

# example no 4
numbers = [1, 2, 3, 4, 5, 6]
even_num = [num for num in numbers if num % 2 == 0]
print(even_num)

# even or odd
numbers = [1, 2, 3, 4, 5]
even_odd = ["Even" if x % 2 == 0 else "odd" for x in numbers]
print(even_odd)

# Q3.

# Create a program that:
# 1. Has a list of numbers: 
# [5, 10, 15, 20, 25]
# 2. Uses a list comprehension to create a new list with only numbers greater 
# than 15
# 3. Prints the new list

numbers = [5, 10, 15, 20, 25]
new_list = [nums for nums in numbers if nums > 15]
print(new_list)