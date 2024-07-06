#list
"""S.no	Method	Description
1	append()	 Used for appending and adding elements to the end of the List. 
2	copy()	It returns a shallow copy of a list
3	clear()	This method is used for removing all items from the list. 
4	count()	These methods count the elements
5	extend()	Adds each element of the iterable to the end of the List
6	index()	Returns the lowest index where the element appears. 
7	insert()	Inserts a given element at a given index in a list. 
8	pop()	 Removes and returns the last value from the List or the given index value.
9	remove()	Removes a given object from the List. 
10	reverse()	 Reverses objects of the List in place.
11	sort()	Sort a List in ascending, descending, or user-defined order
12	min()	Calculates the minimum of all the elements of the List
13	max()	Calculates the maximum of all the elements of the List"""

#list is enclosed with []
#The list can be of any data type
#it is mutable mutble meaning -whenever we want  ,we can change

list=[1,2,3,4,5,6,"ishaq","azar","shahul","riyaz"]
#index starts with 0 as usual
print(list[0])
print(list[8])
print(list[0:]) #slicing
print(list[:])
print(list[3:6])
print(list[1:8])
print(list[:8])
print(list[0:8:2]) #slicing with step
print(list.index("ishaq"))
print(list)
list.append([100,"irfan,billa,nasrulla",10000])
print(list)
list.extend([100,"irfan,billa,nasrulla",10000])
print(list)
print(list.count(4))
list.remove("shahul")
print(list)
list.pop(4)
print(list)
list.reverse()
print(list)
list.insert(0,6)
print(list)
list[0]=5
print(list)
list.insert(0,6)
print(list)
list.clear()
print(list)


#tuple is also like list,but it is immutable
#immutable -we can't change

b=[1,9,4,0,3,8,2,7]
b.sort()
print(b)
print(max(b))
print(min(b))
print(b)