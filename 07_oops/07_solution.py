# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model


    # def general_description(self):
    #     return "Car car car car"    # or
    @staticmethod
    def general_description():  
        return "Car car car car"

my_car = Car("Toyota", "Camry")
print(Car.general_description())