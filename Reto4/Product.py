from datetime import datetime

class Product:
    
    def __init__(self, id:int, name:str, price:float):
        self.id = id
        self.name = name 
        self.price = price 
        self.price_history = {}
        now = datetime.now()
        self.price_history[now] = price
    
    def update_price(self, new_price:float):
        self.price = new_price 
        now = datetime.now()
        self.price_history[now] = new_price
    
    def get_price(self) -> float: 
        return self.price  