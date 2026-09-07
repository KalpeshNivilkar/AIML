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