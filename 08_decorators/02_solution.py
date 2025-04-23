# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args) # str(arg) means converting args into string
        kwargs_value = " ,".join(f"{key}:{value}" for key, value in kwargs.items())
        print(f"Calling fun name i.e {func.__name__} with args {args_value}, and with kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper  

@debug
def great(name,greeting):
    print(f"{greeting} {name}")
great("sanjay",greeting="Hello")


@debug
def hello(name,job):
    print("Hi")

hello("Sanjay",job="Developer")





# def debug(func):
#     def wrapper(): 
#         return func  
#     return wrapper
# @debug
# def hello():
#     print("hello")

# 1st it call hello function it is decorates with debug function so,it go debug function and then call hello function 
   # then it store wrapper func then again down wrapper fun is return now it visit to wrapper function def where again fun is return then it go to hello function and print

# chatgpt explanation

# 1st: Python sees the hello() function is decorated with @debug,
#      so it immediately calls debug(hello) during the definition phase.

# 2nd: Inside debug(), the wrapper() function is defined and returned.

# 3rd: Now, hello = wrapper. So when we call hello(), we are actually calling wrapper().

# 4th: When wrapper() is called, it runs func(), which is the original hello() function.

# 5th: Inside the original hello(), it prints "hello".
