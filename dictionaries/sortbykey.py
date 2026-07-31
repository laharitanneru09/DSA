#   code to sort dictionary by key

dict1 = {"c": 30, "a": 10, "d": 40, "b": 20}

sorted_dict = {}

for key in sorted(dict1):
    sorted_dict[key] = dict1[key]

print("Sorted Dictionary:", sorted_dict)

# Time Complexity : O(n log n)
# Space Complexity : O(n)

#   Alternate method
#   sorted_dict = dict(sorted(dict1.items()))