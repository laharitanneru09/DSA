#finding the sum of values in a dictionary
dct={'n1':23,'n2':16,'n3':10,'n4':13}
total=0
for value in dct.values():
    total+=value
print("The sum of values is:")
print(total)

 #time complexity: O(n)
 #space complexity:O(1)   


 #alternate method:
 #print(sum(dct.values()))
 #time complexity : O(n)
 #space complexity : O(1)