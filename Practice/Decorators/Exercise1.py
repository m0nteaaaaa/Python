# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
    def wrapper(*args, **kwargs):
        if user1.get('valid'):
            return fn(*args, **kwargs)
        else:
            return print("invalid user")
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
