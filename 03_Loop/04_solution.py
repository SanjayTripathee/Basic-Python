#Problem: Reverse a string using a loop.

string = input("Enter a string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string # note not reversed_string = reversed_string + char
print("Reversed string:",reversed_string)