#code to find the second smallest number in the list
lst=[2,43,98,67,54]
smallest = lst[0]
second_smallest = None

for i in range(1, len(lst)):
    if lst[i] < smallest:
        second_smallest = smallest
        smallest = lst[i]
    elif lst[i] != smallest:
        if second_smallest is None or lst[i] < second_smallest:
            second_smallest = lst[i]

if second_smallest is None:
    print("There is no second smallest element.")
else:
    print("Second smallest number:", second_smallest)

#Time complexity : O(n)
#Space complexity :O(1)


#Alternate method:
#find the smallest element in the list 
#create a new list by excluding all its occurrences.
#Then find the smallest element in the new list.
#which will be the second smallest element in the original list.

#Time complexity:O(n)
#Space complexity:O(n)