# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
 # in program think instance is object i.e instance = object
class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):  
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", 75)
car = Car("Toyota", "Camry")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))  
print(isinstance(car, ElectricCar))  