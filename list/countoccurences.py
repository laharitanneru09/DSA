#code to find the number of occurences of an element
list1=[23,87,6,3,2,3,4,7,6,1]
count=0
key=int(input("Enter an element : "))

for i in list1:
   if i==key:
        count+=1
print("The number of occurences of the element is ",count)

# Time Complexity: O(n)
# Space Complexity: O(1)

# Alternate method:
# use count = list1.count(key)