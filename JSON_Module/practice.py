
# . Create a Python dictionary of 3 cities and their populations. Save it to 
# . 
# 1. Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population  - update this info in the json 
# file.

'''import json

# Load existing JSON data
with open("cities.json", "r") as f:
    data = json.load(f)

print("---- existing data ----")
print(data)

# Add new cities
for i in range(int(input("How many new cities do you have to add: "))):

    key = input("Enter name of city: ")
    value = int(input("Enter the population: "))

    data[key] = value

# Save updated dictionary to JSON
with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)

print("---- updated data ----")
print(data)'''

# repractice

'''import json

#read the data
with open("cities.json","r") as f:
    data = json.load(f)
print("----existing data----")
print(data)

# taking input from the users
n = int(input("enter how many time you have to add data: "))
for i in range(n):
    key = input("enter the name of city: ")
    value = int(input(f"enter the population of {key}"))
    data[key] = value

# update the data inside a File 
with open("cities.json","w") as f:
    json.dump(data, f, indent= 4)

# show the data 
print("---updated data---")
print(data)'''

# Create a Python program that:

# Creates a dictionary containing information about a student:
# name
# age
# course
# Saves the dictionary into student.json.
# Loads the JSON file.
# Prints the student's information.

'''import json

with open("student.json","r") as f:
    data = json.load(f)
print("---student info---")
print(data)'''

# Create a Python program that:

# Creates a dictionary containing 3 employees and their salaries.
# Saves the dictionary into employees.json.
# Loads the JSON file.
# Prints each employee's name and salary.

'''import json

employees = {
    "kalpesh": 20000,
    "ram": 30000,
    "vivek":1000
}

with open("employees.json","w") as f:
    json.dump(employees,f,indent=4)

with open("employees.json","r") as f:
   data = json.load(f)
print("---employees data---")
print(data)
'''

# Create a Python program that:

# Creates a dictionary containing 3 products and their prices.
# Saves it into products.json.
# Loads the JSON file.
# Prints each product and its price.
# Asks the user for one new product and its price.
# Adds the new product to the dictionary.
# Updates products.json.

import json

# create a product dict 
products= {
    "Mobile": 20000,
    "TV": 40000,
    "Laptop": 200000
}

# load data into json file 
with open("products.json","w") as f:
    json.dump(products,f,indent=4)

# print existing products
with open("products.json","r") as f:
    data = json.load(f)
print("---existing data---")
print(data)

# add new product possibility
add_product = input(f"you want to add product yes or not:ie = yes or no: ")
if add_product == "yes":
    product_num = int(input("how many product you have to add:"))

    for i in range(product_num):
        key = input("name of product: ")
        value = int(input("price of the product: "))

        data[key] = value

elif add_product == "no":
    print("existing data")
    print(data)

else:
    print("invalid choice.....")

# add data
with open("products.json","w") as f:
    json.dump(data,f,indent=4)

print("----updated data---")
print(data)