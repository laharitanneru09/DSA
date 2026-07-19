# A code to count the number of vowels in string

str1=input("Enter a string : ")
count=0
for i in str1:
    if i in {'a','e','i','o','u','A','E','I','O','U'}:
        count+=1
print("Number of vowels : ",count)

#Time Complexity : O(n)

#Space Complexity : O(1)


#Alternate method
#count = sum(1 for i in str1 if i.lower() in "aeiou")
#Time complexity :O(n)
#Sapce Complexity : O(1)