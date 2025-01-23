#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('cindy',2)
cat2 = Cat('tyler',5)
cat3 = Cat('mike',9)

# 2 Create a function that finds the oldest cat
def OldestCat(age1,age2,age3):
    if cat1.age > cat2.age & cat1.age > cat3.age:
        print(cat1.age)
    elif cat2.age > cat1.age & cat2.age > cat3.age:
        print(cat2.age)
    else:
        print(cat3.age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {OldestCat(cat1.age,cat2.age,cat3.age)} years old')


'''
# Exercise Cats Everywhere

# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
'''