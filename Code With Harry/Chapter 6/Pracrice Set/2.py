# WAP to find if a student is pass or fail . If it requires total 40% and at least 33% in each subject to pass . Assume 3 subjects and take marks input from the user.

subject1 = int(input("Enter marks : "))
subject2 = int(input("Enter marks : "))
subject3 = int(input("Enter marks : "))

total = ((subject1 + subject2 + subject3)/3)*100
if(total>33):
    if (subject1 and subject2 and subject3 > 40):
        print("Pass")
    else:
        print("Fail")