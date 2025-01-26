some_list = ['a','b','c','b','d','m','n','n']
 
my_set = {item for item in some_list if some_list.count(item)>1}
print(list(my_set))