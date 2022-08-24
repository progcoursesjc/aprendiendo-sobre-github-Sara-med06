from datetime import date
from itertools import product
from Product import Product
from Order import Order
from User import User


user_1 = User(1044, "fernando", 500)

# Products
product_1 = Product(1, "marcador", 20)
product_2 = Product(2, "cuaderno", 13)
product_3 = Product(3, "libro", 100)
product_4 = Product(4, "tijeras", 20)
product_5 = Product(5, "lapìcero", 400)

# First order
user_1.add_product_to_car(product_1)
user_1.add_product_to_car(product_2)
user_1.add_product_to_car(product_3)
user_1.add_product_to_car(product_5)
user_1.consolidate_order()

# Second order
user_1.add_product_to_car(product_4)
user_1.add_product_to_car(product_3)
user_1.add_product_to_car(product_3)
user_1.consolidate_order()


user_1.plot_order_history()