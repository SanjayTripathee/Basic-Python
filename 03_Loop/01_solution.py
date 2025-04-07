# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# for num in numbers:
#     if num > 0:
#         print(num)

# above solution is what i though at begning question is telling me but after looking tutural i understand actual meaning of question

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1

print("Number of positive numbers:", positive_count)



