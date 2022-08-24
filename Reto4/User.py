import matplotlib.pyplot as plt
import numpy as np

from Product import Product
from Order import Order

class User:
    def __init__(self, id:int, user_name:str, balance:float):
        self.id = id
        self.user_name = user_name 
        self.balance = balance
        self.order_list = []
        self.current_order = None
    
    def add_product_to_car(self, prod:Product):
        if self.current_order is None:
            order_id = len(self.order_list) + 1
            self.current_order = Order(order_id)

        new_total = prod.get_price() + self.current_order.get_total()
        if self.balance < new_total:
            print("insuficient balance")
        else: 
            self.current_order.add_product(prod)


    def add_to_balance(self, amount:float):
        self.balance += amount
    
    def consolidate_order(self):
        if self.current_order is None: 
            print("There isn't a current order to consolidate")
        else:
            self.balance -= self.current_order.get_total()
            self.current_order.set_status(False)
            self.order_list.append(self.current_order)
            self.current_order = None

    def plot_order_history(self):
        ids    = []
        totals = []
        for order in self.order_list:
            ids.append(order.get_id())
            totals.append(order.get_total())

        x_points = np.array(ids)
        y_points = np.array(totals)

        plt.plot(x_points, y_points)
        plt.show()
