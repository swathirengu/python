input_str = "swathi"

print("original string: " + input_str)

result_str = ""

for i in range(0, len(input_str)):
    if i != 4:
        result_str = result_str + input_str[i]

    # Printing string after removal
print("String after removal of i'th character : " + result_str)
