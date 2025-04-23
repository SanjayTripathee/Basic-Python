# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

class Engine:
    def __init__(self, engine_size):
        self.engine_size = engine_size  

class ElectricCar(Battery, Engine):
       def __init__(self,battery_size,engine_size,model):
            Battery.__init__(self, battery_size)
            Engine.__init__(self,engine_size)
            self.model = model
electric = ElectricCar("11 s","11 p","Model S")
print("Model is: ",electric.model)
print("Battery size is: ",electric.battery_size)
print("Engine size is: ",electric.engine_size)
            


# class Battery:
#     pass