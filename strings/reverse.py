# printing the reverse of a string without using slice
#method-1 : using indexing(optimized method)
str1=input("Enter a string  : ")
reverse = ""
for i in range(len(str1) - 1, -1, -1):
    reverse += str1[i]
print("Reversed string : ",reverse)
#time complexity:O(n)
#space complexity:O(n)


#Alternate method
#for char in str1:
#    reverse = char + reverse
#time complexity : O(n^2)
#space complexity:O(n)

