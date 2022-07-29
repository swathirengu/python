def computegcd(a,b):
    if b==0:
        return a
    else:
        return computegcd(b,a%b)
num1=int(input("enter the first number "))
num2=int(input("enter the second number"))
print(computegcd(num1,num2))
