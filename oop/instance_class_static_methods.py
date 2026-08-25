'''we have a product and product price,
we have to cal total numbers of product.
also we have to calculate the discount by given percentage.'''

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"The price of {self.name} is {self.price}")

    # count_product
    @classmethod
    def count_product(cls):
        print(f"The total number of product is {cls.count}")

    # cal_discount
    @staticmethod
    def cal_discount(price, percentage):
        print(f"The total discount is {price - (price * percentage / 100)}")

p1 = Product("laptop", 30000)
p2 = Product("Tv",50000)

Product.count_product()             
p1.get_info()
p1.cal_discount(p1.price,10)

# output
# The total number of product is 2
# The price of laptop is 30000
# The total discount is 27000.0
#i like to learn this concept..so nice to learn this concept.



        