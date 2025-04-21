# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand
# my_car = Car("Tata", "Camry")
# print(my_car.get_brand()) 


# adding setter method

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    def set_brand(self,new_brand):
        self.__brand = new_brand
my_car = Car("Tata", "Camry")# getter obj
print(my_car.get_brand()) 

my_car.set_brand("Honda")# setter obj
print(my_car.get_brand())      