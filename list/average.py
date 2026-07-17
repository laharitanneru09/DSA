#finding the average of the values in the list
lst=[12,2,4,6,7,9]
sum=0

for ele in lst:
    sum+=ele

avg=sum/len(lst)
print(avg)
#Time complexity: O(n)
#Space complexity:O(1)

#Alternate method
#using avg = np.mean(lst)
#Time complexity: O(n)
#Space complexity:O(1)
