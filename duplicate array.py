arr=[1,2,3,16,58,16,3,4,100,98,100]

print("Duplicate elements in the array:")
for i in range(0,len(arr)):#select the element
    for j in range(i+1,len(arr)):#compare the selected element
        if(arr[i]==arr[j]):
            print(arr[j])