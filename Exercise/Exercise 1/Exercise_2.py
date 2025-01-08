username = input("Enter your user name : ")
password = input("Enter your password : ")
encrypted = '*' * len(password)
print(f"Hello {username} You're password is {encrypted} and its length is {len(password)} long") 