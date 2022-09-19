from datetime import datetime

class Thing:
    def __init__(self, name:str):
        self.name = name

class Place: 
    def __init__(self, name:str):
        self.name = name

class User: 
    def __init__(self, dniType:str, dni:str, name:str, rol:str):
        self.dniType = dniType
        self.dni = dni
        self.name = name
        self.rol = rol 
    
    def bookReservation (self, place:Place, datetime, thing:Thing):
        reservation = Reservation(self, place, datetime, thing)
        return reservation

class Reservation: 
    def __init__(self, user:User, place:Place, datetime:datetime, thing:Thing):
        self.user = user
        self.place = place
        self.thing = thing
        self.datetime = datetime
