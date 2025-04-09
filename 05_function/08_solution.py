# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# def print_kwargs(**kwargs):
#     for key in kwargs:
#         print(key, ":", kwargs[key])



# print(print_kwargs(a=1, b=2, c=3))

def pair(name,value):
    print(name,":",value)

pair("a",1)
pair("b",2)
pair("c",3)
   