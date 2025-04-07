#   strip is ? (down is defination with example)
#Removes spaces from a string.
# eg : text = "  Dog  "
#print(text.strip())  # Output: "Dog"


animal = input("Enter animal (dog/cat): ").strip().lower()
age = int(input("Enter the age:"))

if(animal == "dog" and age<2):
    print("Puppy food")
elif(animal == "cat" and age>5):
    print("Senior Cat food")
else:
    print("non condition match")
  

