i=1
guess_number=18
count=10
while i<10:
    number=int(input("enter the number:"))
    if number>18:
        print("it is bigger ")
    elif number<18:
        print("it is lesser")
    elif number==18:
        print("you have entered correct number")
        count=count-1
        print("you have finished with in",count,"chance")
        break
    count=count-1
    print("you have ",count,"chance left")
    i+=1