# Error Handling

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeErrors as err:
        print('Please! enter numbers ' + err)
    
print(sum('1', 2))

def sol(num1, num2):
    try:
        return num1 / num2
    except (TypeErrors, ZeroDivisonError) as err:
        print('Please! enter numbers ' + err)
    
print(sum('1', 2))