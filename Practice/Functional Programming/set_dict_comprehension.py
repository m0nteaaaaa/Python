my_list = {char for char in 'hello'}
print(my_list)

my_list2 = {num for num in range(0,11)}
print(my_list2)

my_list3 = {num**2 for num in range(0,11)}
print(my_list3)

my_list4 = {num**2 for num in range(0,11)
            if num%2 == 0 }
print(my_list4)

simple_dict = {'a':1,'b':2}
my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict)

my_dict1 = {num:num*2 for num in [1,2,3]}
print(my_dict1)