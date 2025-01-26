from functools import reduce

my_list= [1,2,3]

def accmulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))