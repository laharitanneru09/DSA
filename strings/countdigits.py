# finding the number of digits in the string
str1=input("Enter a string : ")

count=0

for ch in str1:
    if '0' < ch < '9':
        count+=1

print("The number of digits in the string is : ",count)

#Time complexity : O(n)
#Space complexity : O(1)

#Alternate method
#we can use isdigit instead of '0' < ch < '9'
# or just do count = sum('0' <= ch <= '9' for ch in str1)
#but all of these will have same O complexities