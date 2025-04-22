# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer  # now i use timer function decorator so,when i call example_func it will first pass from timer function and then pass to example_func
def example_func(n):
    time.sleep(n)

example_func(2)