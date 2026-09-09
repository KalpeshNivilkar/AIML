import json

# Load existing data from JSON file
with open("pis_product_data.json", "r") as f:
    data = json.load(f)


while True:

    print("\n--- Welcome to Product Inventory System ---")
    print("1. View Product")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Search Product")
    print("5. Delete Product")
    print("6. Exit")

    number = int(input("Enter your choice: "))


    # 1. View Product
    if number == 1:

        print("\n--- Existing Products ---")

        for product, price in data.items():
            print(f"{product} : {price}")

        print("Data loaded successfully...")


    # 2. Add Product
    elif number == 2:

        n = int(input("How many products do you want to add: "))

        for i in range(n):

            product = input("Enter the name of product: ")
            price = int(input("Enter the price: "))

            data[product] = price

        print("Data added successfully...")


    # 3. Update Product
    elif number == 3:

        product = input("Enter the name of product: ")

        if product in data:

            price = int(input("Enter the updated price: "))

            data[product] = price

            print(f"{product} updated successfully...")

        else:

            print(f"{product} is not found...")


    # 4. Search Product
    elif number == 4:

        product = input("Enter the name of product: ")

        if product in data:

            print(f"{product} : {data[product]}")

        else:

            print(f"{product} is not found...")


    # 5. Delete Product
    elif number == 5:

        product = input("Enter the name of product to delete: ")

        if product in data:

            del data[product]

            print(f"{product} deleted successfully...")

        else:

            print(f"{product} is not found...")


    # 6. Exit
    elif number == 6:

        print("Thank you for using Product Inventory System!")
        break


    # Invalid choice
    else:

        print("Invalid choice!")


    # Save updated data to JSON file
    with open("pis_product_data.json", "w") as f:
        json.dump(data, f, indent=4)