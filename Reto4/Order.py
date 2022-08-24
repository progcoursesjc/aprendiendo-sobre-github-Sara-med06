from datetime import date
from Product import Product

class Order:

    def __init__(self, id:int):
        self.id = id 
        self.product_list = []
        self.date = date.today()
        self.total = 0
        self.status = True
    
    def get_id(self) -> int:
        return self.id
    
    def get_total(self) -> float: 
        return self.total

    def add_product(self, prod:Product):
        self.total += prod.get_price()
        self.product_list.append(prod)

    def set_status(self, new_status:bool):
        self.status = new_status
        return self
    