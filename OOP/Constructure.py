"""
__init__()
"""

class Car:
    #method
    def set_details(self, name, color):
        self.name = name
        self.color = color
    
    def show_details(self):
        print(f"This is an {self.color} {self.name}")

car01 = Car()
car01.set_details("BMW", "Black")

car01.show_details()

class Car_constructure:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def show_details(self):
        print(f"This is an {self.color} {self.name}")

car03 = Car_constructure('BMW', "Black")
car03.show_details()