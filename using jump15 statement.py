while True:
    number=int(input("enter the number which should be greater than 100:"))
    if number<=100:
        print("try again")
        continue
    else:
        print("you won")
        break