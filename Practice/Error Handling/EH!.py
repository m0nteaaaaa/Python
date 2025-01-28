#Error Handling

while (True):
    try:
        age=int(input('What is yout age :'))
        10/age
    except ValueError:
        print('PLEASE!! enter a NUMBER!!!')
    except ZeroDivisonError:
        print('PLEASE!! enter a number higher than 0 ')
    else:
        print('Thank you')
        break