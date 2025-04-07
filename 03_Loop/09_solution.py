
#Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

strng = "snjay"

for char in strng:
    if strng.count(char)>1:
        print(char,"is duplicate char")
        break
    else:
        print(char,"is unique char")
    