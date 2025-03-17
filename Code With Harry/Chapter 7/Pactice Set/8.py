# WAP to calculate the factorial of a given number using for loop

fact = 1
n = int(input("Enter number : "))
for i in range(1,n+1):
    fact = fact*i
    i = i + 1
print(fact)