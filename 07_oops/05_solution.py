# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or desel" 
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electricity Consume"
 
my_car = Car("Toyota", "Camry")
print(my_car.fuel_type())

my_tesla = ElectricCar("Tesla", "Model S", 75)
print(my_tesla.fuel_type())



