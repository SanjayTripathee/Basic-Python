# Problem: Create a recursive function to calculate the factorial of a number.
 #A recursive function is a function that calls itself in order to solve a problem.  until it reaches a point where it can stop calling itself 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # here it is calling a fun itself
 
print(factorial(5)) 