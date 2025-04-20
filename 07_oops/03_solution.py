# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
 

my_tesla = ElectricCar("Tesla", "Model S", 75)
print("Brand is: ",my_tesla.brand)
print("Model is: ",my_tesla.model)
print("Battery size is: ",my_tesla.battery_size)

