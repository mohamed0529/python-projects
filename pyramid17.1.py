n=int(input("enter the num:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("j",end=" ")
    print()