#  Problem: Create a function that returns both the area and circumference of a circle given its radius.

r = 1
area = 3.14 * r * r
circum = 2 * 3.14 * r

def cirle(r):
    return area, circum 

# result = cirle(2)
# print("Area and Circumference is: ",result)
print("Area and Circumference is: ",cirle(2))


