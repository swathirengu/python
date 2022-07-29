num=int(input("enter the number:"))
org=num
Rev = 0
while(num > 0):
     rem = num % 10
     rev = rev * 10 + rem
     num = num // 10
print("the reverse of",org,"is",rev)
if  org== rev:
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")