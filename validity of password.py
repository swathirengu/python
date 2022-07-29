import re
flag=0

passwd=(input("enter the passwd"))

if not re.search('[a-z]',passwd):
    flag=1
if not re.search('[0-9]',passwd):
    flag=1
if not re.search('[A-Z]',passwd):
    flag=1
if not re.search('[$@*]',passwd):
    flag=1
if len(passwd)<10:
    flag=1
if (flag==0):
    print(" the password is valid ")
else:
    print("the password is invalid")