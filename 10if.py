#conditional statement
#if elif else

#elgible to drive
age=int(input("how old are you:"))

if age>=18 and age<55 and age>0 :
    print("you can drive")
elif age >=55:
    print("you are too aged person so ,you can't drive")
elif age==0:print("you havent birth")
else:
    print("you can't drive because you do not have valid lisence ")




   # nested loop

a=int(input('enter the number:'))
if a>0:
    print("positive")
    if(a%2==0):
        print("even number")
    else:print("odd")
elif a==0:
    print("zero")
else:
    print('negative')