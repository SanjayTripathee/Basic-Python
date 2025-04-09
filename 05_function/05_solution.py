# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

# name = input("Enter your name: ")
# great = f"Hello  {name}"


# def func(name):
#     if name.strip():
#         print(great)
#     else:
#         print("Hello Sanjay")

# func(name)


# or,,,,,

def func(name="sanjay"):
    print(f"Hello {name}")

func()

