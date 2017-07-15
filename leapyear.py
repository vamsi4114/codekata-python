year = int(input("enter the year to be checked:"))
if((year % 4 ==0) and (year % 100 !=0)):
    print("this is a leap year")
elif (year % 100==0):
    print("this is not a leap year")
elif (year % 400 ==0):
    print("this is a leap year")
    
