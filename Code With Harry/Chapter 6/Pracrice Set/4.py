# WAP to find wether a given username cointains less than 10 characters or not.

name = input("Enter name : ")
if (len(name) < 10):
    print("Less than 10")
else:
    print("Greater than 10")