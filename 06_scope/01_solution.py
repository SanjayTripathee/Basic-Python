# userName = "Sanjay"

# def name():
#     userName = "Chandu"
#     print(userName)

# name()
# print(userName)

# closure concept

# def outer():
#     num1 = 10
#     def inner():
#         num2 = 20
#         print(num1)
#         print(num2)
#     inner()

# outer()


# another eg:

# def outer(num):
#     def inner(x):
#         return x**num
#     return inner

# a = outer(2)
# b = outer(3)
# print(a(2))
# print(b(3))
