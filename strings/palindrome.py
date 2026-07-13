# program to check whether a given string is palindrome or not
s = input("Enter a string : ")

for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        print("Not a palindrome")
        break
else:
    print("Palindrome")

#time complexity : O(n)
#space complexity : O(1)

#Alternate method 
#using slicing and check whether s == s[::-1]
#time complexity : O(n)
#space complexity : O(n)