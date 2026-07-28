#finding the frequency of a character in given string
string1=input("Enter a string : ")
char=input("Enter a character to find its frequency : ")
count=0
if len(char) != 1:
    print("Please enter only one character")
else:
    for ch in string1:
        if ch == char:
            count+=1
    print("The frequency of the character is ",count)

#   Time Complexity :  O(n)
#   Space Complexity:  O(1)


#   Alternate method
#   use count = string1.count(char)

