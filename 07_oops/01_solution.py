# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
  # instance means eg:- but in program think instance is object so, in question. it is telling to create an object of car
# remenber class name first letter must be capital like Car here in below eg
class Car:
    def __init__(self,brand,model):  # Yes, exactly __init__ takes parameters so you can pass values when creating the object.(It is constructor)
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Camry")# my_car is an object
ccar = Car("Honda", "Civic")# another object created
print(my_car.brand)
print(my_car.model)
print(ccar.brand)

# self is like js this keyword.  Self is like telephone wire to connect 


# js with this eg:

# class Person {
#     constructor(name) {
#         this.name = name; // 'this' refers to the current object
#     }

#     greet() {
#         console.log(`Hello, my name is ${this.name}`);
#     }
# }

# const p = new Person("Alice");
# p.greet();

