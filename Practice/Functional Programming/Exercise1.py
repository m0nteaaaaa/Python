from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
#map
def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the 
#numbers from lowest to highest.

#zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings,sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def check_pass(marks):
    return marks > 50

print(list(filter(check_pass, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc,items):
    return items + acc

print(reduce(accumulator,(my_numbers + scores)))