s="hello swathi"
c={}
for i in s:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
    print(c)