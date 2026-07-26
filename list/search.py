#code to search for an element in a list
list1=[2,8,56,42,12,8]
key=int(input("Enter a number to search : "))
found = False

for i in range(len(list1)):
    if list1[i]==key:
        found=True
        print("Element found in index ",i)
        

if not found :
    print("Element not found")

#Time complexity : O(n)
#Space Complexity : O(1)

# Alternative:
# If the list is sorted 'Binary Search' can be used.
# Time Complexity: O(log n)
# Space Complexity: O(1)