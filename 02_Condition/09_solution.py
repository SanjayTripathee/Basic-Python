leap_year = 2000

if(leap_year % 400 == 0) or (leap_year % 4 == 0 and leap_year % 100 != 0 ):
        print("This is leap year")
else:
    print("Not leap year")
