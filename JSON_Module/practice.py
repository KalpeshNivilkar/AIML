
# . Create a Python dictionary of 3 cities and their populations. Save it to 
# . 
# 1. Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population  - update this info in the json 
# file.

import json

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
print(data)


    