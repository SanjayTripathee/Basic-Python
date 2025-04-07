age = 160
day = 'wednesday'
price = 12
# price = 12 if age > 18       else 8

if(age<18):
    price = 8
elif(age>=18 and age < 60):
    price = 12
else:
    price = 7
  


if day == 'wednesday':
    price -= 2 #price = price - 2

print("Price of ticket is RS:",price)