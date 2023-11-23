'''
@DEFINITION - A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that will be associated with the objects created from the class.
'''

# Creating a class using 'class' keyword
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model}")

# Creating object instances
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")
