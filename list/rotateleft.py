#   code to rotate a list to the left by k positions

def reverse(lst,start,end):
    while start <  end:
        lst[start],lst[end]=lst[end],lst[start]
        start+=1
        end-=1



list1=[1,2,3,4,5]
k=int(input("Enter k value : "))

k=k % len(list1)
reverse(list1,0,k-1)
reverse(list1,k,len(list1)-1)
reverse(list1,0,len(list1)-1)

print(list1)

#   Time Complexity : O(n)
#   Space Complexity : O(1)