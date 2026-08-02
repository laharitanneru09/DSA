# code to reverse the list
lst1=[12,13,14,15,16]

print("List before reversing is : ",lst1)

left=0
right=len(lst1)-1
while left<right:
    lst1[left],lst1[right]=lst1[right],lst1[left]
    left+=1
    right-=1


print("List after reversing is : ",lst1)

#Time complexity:O(n)
#space complexity:O(1)

