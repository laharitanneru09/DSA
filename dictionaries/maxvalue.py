#Finding the key with max value in the dictionary
my_dict = {"n1": 80, "n2": 45, "n3": 67, "n4": 56}

min_key = list(my_dict.keys())[0]
min_value = my_dict[min_key]

for key in my_dict:
    if my_dict[key] < min_value:
        min_value = my_dict[key]
        min_key = key

print("Key with minimum value:", min_key)
print("Minimum value:", min_value)
#Time Complexity: O(n)
#Space complexity:O(1)


#Alternate method : using built-in function
#min_key = min(my_dict, key=my_dict.get)
#for this method 
#Time Complexity: O(n)
#Space complexity:O(1)

