#   Sorting the dictionaries by value
#   Brute force method
dict1 = {"c": 90, "a": 100, "d": 40, "b": 20}
values = []

for key in dict1:
    values.append(dict1[key])

# Bubble Sort
n = len(values)

for i in range(n):
    for j in range(n - i - 1):
        if values[j] > values[j + 1]:
            temp = values[j]
            values[j] = values[j + 1]
            values[j + 1] = temp
            
sorted_dict = {}

for value in values:
    for key in dict1:
        if dict1[key] == value and key not in sorted_dict:
            sorted_dict[key] = value
            break

print(sorted_dict)


#Time Complexity : O(n^2)
#Space Complexity : O(n)

#Optimised method:
#Using sorted() function
