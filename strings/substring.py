#program to check whether a substring exists in a string
str1=input("Enter the main string : ")
substr=input("Enter the substring : ")

if substr in str1:
    print("Substring exists.")
else:
    print("Substring does not exist.")
# Time Complexity: O(n*m)
# where m is size of mainstring and n is size of substring
# Space Complexity: O(1)

#Alternate method
# Compare each possible position manually using loops.
# Time Complexity: O(n*m)
# Space Complexity: O(1)