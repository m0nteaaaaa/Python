#List (Mutable)(Ordered)
lists =  ['hello',10,4.6]
marks = [10,2,5,99,10,6.99]
print(type(marks))
print(marks)

#indexing
print(marks[0])

marks[0] = 99
print(marks)

#slicing
print(marks[1:3])

#Methods
marks.append(3)
marks.sort()
marks.sort(reverse=True)
marks.reverse()
marks.insert(0,10)

#Tuples (unordered)(immutable)
tup = (74,54,2,34,23)

#no indexing
tup1  = (1,) #for single tuple

#Methods
tup.index(54)
tup.count(2)

#Practice

mov1 = input("Enter Movie : ")
mov2 = input("Enter Movie : ")
mov3 = input("Enter Movie : ")

list = []
list.append(mov1)
list.append(mov2)
list.append(mov3)
print(list) 

#Practice

#[1,2,3,2,1] or [1,'abc','abc',1]

list1 = [1,2,3,2,1]
list2 = []
list2 = list1.copy()
list2.reverse()
print(list1)
print(list2)
if list1 == list2:
    print("Palindrome")
else:
    print("Not Palindrome")