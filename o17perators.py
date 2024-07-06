#today i'm gonna learn about operators
#types of operators in python
"""1.arithmetic
2.assignment
3.comparision
4.logical
5.identify
6.membership
7.bitwise"""
#1.arithmetic operator- it is nothing but mathematical calculation
#eg:
print(5+5) #this is for adding two operands
print(6-8)# this is for subtracting
print(10%5)# this is for finding reminder with divide
print(19//5)# this is for dividing 
print(19/5)#this is for dividing
print(10*8)#multiple
print(10**2)#exponential (power)


#assignment operatos
#it is nothing but assigning value

a=6
b=10
print(a)
print(b)

#comparision operator

#  == -it is for comparing two operands whether both are equal or not


# < 
# >
# >=                 it is all for checking whether operand bigger or smaller
# <=

#logical                                      true and true = true   otherwise false
#and                                          false or false =false othereise true
#or
#not
a=6
b=9
c=7
print(a<b and c>a)
print(a<3 and b>c)
print(a<3 or b>c)
print(a<3 or b>100)


#identity (key word is nothing but "is")

a=6
b=6
c=7

print(a is b,a is c)
print(a is not b,a is not c)

#membership                 keyword(in)

a=[1,2,3,4,5,6]
print(1 in a)
print(2 in a)
print(100 in a)
print(6  not in a)