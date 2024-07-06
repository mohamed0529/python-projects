"""A while loop evaluates the condition
If the condition evaluates to True, the code inside the while loop is executed.
condition is evaluated again.
This process continues until the condition is False.
When condition evaluates to False, the loop stops."""

"""i=1
while i<=5:
    print("mohamed ishaq")
    i+=1"""

"""i=2
while i<50:
    print(i)
    i+=1"""

#making table

number=int(input("enter the table:"))
#number=5
i=1
while i<=20:
    product=i*number
    print(i,"x",number,"=",product)
    i+=1