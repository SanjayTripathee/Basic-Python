# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# def pair(name,value):
#     print(name,":",value)

# pair("a",1)
# pair("b",2)
# pair("c",3)
   

def pair(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

pair(a=1, b=2, c=3)
pair(name="sanjay",Power="selfmade")
pair(f="22")