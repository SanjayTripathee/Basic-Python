# num = int(input("Enter a number: " ))

# for i in range(1,11):
#     if i == range(1,11):
#         break
# print(num)

#Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    num = int(input("Enter a number between 1 and 10: "))
    if num >= 1 and num <= 10:
        break