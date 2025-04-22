# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    car_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count += 1

my_car = Car("Toyota", "Camry")#1
print(my_car.brand)
test = Car("Honda", "Civic")#2
third_car = Car("t","t")#3 
print("Car count is: ",Car.car_count)# op = Car count is: 3 because we arecreating car 3 times