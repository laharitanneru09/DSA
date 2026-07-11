#finding the minimum number in the list
list1=[6,5,7,9,2,3]
min=list1[0]
for i in list1:
    if i<min:
        min=i
print(f"The minimum number in the list is {min}")
#time complexity : O(n)
#space complexity : O(1)

#Alternate method 
#using the built in function print(min(list1))
#time complexity: O(n)
#space complexity: O(1)