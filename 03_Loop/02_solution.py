# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# sum_even = 0

# for num in numbers:
#     if num >= 0 and num % 2 == 0:
#         sum_even += num
# print("sum of even number:",sum_even)

#Problem: Calculate the sum of even numbers up to a given number n.

n = 20
sum_even = 0

for i in range(1,n+1):
    if i%2==0:
        sum_even+=1

print("sum of even number:",sum_even)

