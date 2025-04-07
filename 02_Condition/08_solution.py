# password_length = 8

# if password_length < 6:
#     print("password is week")
# elif password_length < 10:
#     print("password is medium")
# else:
#     print("password is strong")



password_length = 8

if password_length in range(0,6):
    print("password is week")
elif password_length in range(6,10):
    print("password is medium")
else:
    print("password is strong")







