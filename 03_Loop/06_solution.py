#Problem: Compute the factorial of a number using a while loop.

num = 5
factorial = 1
fact_num = num

while num > 0: # it go(loop) upto num is not zero and when 0 exit
    factorial *= num
    num -= 1

print("Factorial of", fact_num, "is", factorial)

#

# num = 5
# factorial = 1

# for i in range(num,0,-1):# -1 means loop downward because num =5 is greater then 0  so we muct loop back to find factorial i.e 5,4,3,2,1
#     factorial *= i

# print("Factorial of", num, "is", factorial)



#


# num = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, num + 1):
#     factorial *= i

# print("Factorial of", num, "is", factorial)


