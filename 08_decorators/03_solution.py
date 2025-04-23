# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
 # meaning of= "Cache Return Values" generally means storing the result of a function or operation so that if the same operation  
  #is performed again with the same input, the cached (previously stored) result is returned instead of recalculating it.

import time
def cache(func):
    cache = {}
    print(cache)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        # if not cashed below will execute
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper


@cache
def expensive_function(*args, **kwargs):
    time.sleep(4)
    return sum(args)

print(expensive_function(1, 2, 3))
print(expensive_function(1, 2, 3))# this will not execute because it is cashed i.e  # Uses cached result of above line
print(expensive_function(2,2,1)) # here args i.e argument is diffn so, it will be recalculate