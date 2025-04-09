# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):# *args is a tuple which accept multiple arguments
    # print(*args)
    # for i in args:
    #     print(i*2)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4))