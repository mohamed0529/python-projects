#function-block of  code
#void-it returns nothing
#non void-it returns something

#example for function

def add():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    return a+b


print(add())


def add1():
    """this function is used for adding two number"""
    a=int(input("enter the number:"))
    b=int(input("enter the number :"))
    print(a+b)


add()


#using parameter 

def add(a,b):
    return a+b
a=int(input("enter the number:"))
b=int(input("enter the number :"))
print(add(a,b))



def add(a,b):
    print(a+b)
a=int(input("enter the number:"))
b=int(input("enter the number :"))
add(a,b)


print(add1.__doc__)