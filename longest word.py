def LongestWordLength(String):
    l= 0
    w=' '
    words= String.split()
    for word in words:
         if(len(word)>l):
          w=word
          l=len(word)
          return(w,l)

string = input("Enter the String:")
w,l=LongestWordLength(string)
print("longest word is:", w)
print("length of longest word is : ",l)