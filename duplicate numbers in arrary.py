# Python3 implementation of the
# above approach

# Function to find the Duplicates,
# if duplicate occurs 2 times or
# more than 2 times in array so,
# it will print duplicate value
# only once at output
def findDuplicates(arr, Len):
    # Initialize ifPresent as false
    ifPresent = False

    # ArrayList to store the output
    a1 = []
    for i in range(Len - 1):
        for j in range(i + 1, Len):

            # Checking if element is
            # present in the ArrayList
            # or not if present then break
            if (arr[i] == arr[j]):
                if arr[i] in a1:
                    break

                # If element is not present in the
                # ArrayList then add it to ArrayList
                # and make ifPresent at true
                else:
                    a1.append(arr[i])
                    ifPresent = True

    # If duplicates is present
    # then print ArrayList
    if (ifPresent):
        print(a1, end=" ")
    else:
        print("No duplicates present in arrays")


# Driver Code
arr = [12, 11, 40, 12, 5, 6, 5, 12, 11]
n = len(arr)

findDuplicates(arr, n)

# This code is contributed by rag2127
# Python3 implementation of the
# above approach

# Function to find the Duplicates,
# if duplicate occurs 2 times or
# more than 2 times in array so,
# it will print duplicate value
# only once at output
def findDuplicates(arr, Len):
    # Initialize ifPresent as false
    ifPresent = False

    # ArrayList to store the output
    a1 = []
    for i in range(Len - 1):
        for j in range(i + 1, Len):

            # Checking if element is
            # present in the ArrayList
            # or not if present then break
            if (arr[i] == arr[j]):
                if arr[i] in a1:
                    break

                # If element is not present in the
                # ArrayList then add it to ArrayList
                # and make ifPresent at true
                else:
                    a1.append(arr[i])
                    ifPresent = True

    # If duplicates is present
    # then print ArrayList
    if (ifPresent):
        print(a1, end=" ")
    else:
        print("No duplicates present in arrays")


# Driver Code
arr = [12, 11, 40, 12, 5, 6, 5, 12, 11]
n = len(arr)

findDuplicates(arr, n)

# This code is contributed by rag2127
