arr=[5,4,3,2,1]
temp=0

print("the original array element is:")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
for i in range (0,len(arr)):
    for j in range (i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print()
print("after sorting the elements in array:")
for i in range (0,len(arr)):

    print(arr[i],end=" ")
