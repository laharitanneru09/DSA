#code to find the second largest number in the list
lst=[2,43,98,67,54]
largest = lst[0]
second_largest = None

for i in range(1, len(lst)):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i] != largest:
        if second_largest is None or lst[i] > second_largest:
            second_largest = lst[i]

if second_largest is None:
    print("There is no second largest element.")
else:
    print("Second largest number:", second_largest)

#Time complexity : O(n)
#Space complexity :O(1)


#Alternate method:
#find the largest element in the list 
#create a new list by excluding all its occurrences.
#Then find the largest element in the new list.
#which will be the second largest element in the original list.

#Time complexity:O(n)
#Space complexity:O(n)