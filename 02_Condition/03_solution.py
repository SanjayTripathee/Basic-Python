# grade = "A"
# if(grade == "A"):
#     print("score =","90-100")

# elif(grade == "B"):
#     print("80-89")

# elif(grade == "C"):
#     print("70-79")

# elif(grade == "D"): 
#     print("60-69")

# elif(grade == "F"):
#     print("below 60")
# else:
#     print("invalid")

#

# grade = 80
# if grade in range(90, 100):
#     print("grade is:","A")
# elif grade in range(80,89):
#     print("grade is:","B")
# elif grade in range(70,79):
#     print("grade is:","C")
# elif grade in range(60,69):
#     print("grade is:","D")
# elif grade in range(0,59):
#     print("grade is:","F")
# else:
#     print("invalid")

#

grade = 1


if(grade>=101):
    print("plze Check the marks again")
    exit()

if(grade>=90):
    print("grade is:","A")  

elif(grade>=80):
    print("grade is:","B")
elif(grade>=70):
    print("grade is:","C")
elif(grade>=60):
    print("grade is:","D")
else:
    print("grade is:","F")