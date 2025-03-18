class car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def properties(self):
        print(f"This is a {self.color} {self.brand}")

car1 = car()
car1.set_details("BMW", "Black")

car2 = car()
car2.set_details("Dodge", "Green")

car1.properties()
car2.properties()