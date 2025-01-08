# Strings
a = 'hello'
b = "hello"
c = '''hello'''

#Escape Sequence
# \n new line
#\t Tab space

#String Operation

# Concatenation
str1 = "Hello"
str2 ="Monty"
str3 = str1 + " " + str2
print(str3)

# Length Function
print(len(str3))

#String Indexing (string assignment is not allowed)
print(str3[1])

#String Slicing (also have negative slicing)
print(str3[1:5:2])
#[start:stop:jump]

#More Functions for String
str1.endswith("er")
str1.capitalize()
str1.replace('a','b') 
str1.find('o') # returns index
str1.count("m") # count how many times it occurs

#Practice
name = input("Enter Your name : ")
print(len(name))

#Practice
strrr = "$kibidi $kin"
print(strrr.count("$"))

#Conditional Statements
# if
# elif
# else

#Practice

marks = int(input("Enter your marks : "))
if marks>=90:
    print("A")
elif 90>marks and marks>=80:
    print("B")
elif 90>marks and marks>=70:
    print("C")
else:
    print("D")