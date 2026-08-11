# Find common keys in two dictionaries

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}

common = {}

for key in dict1:
    if key in dict2:
        common[key] = dict1[key]

print("Common keys =", common)

# Time Complexity : O(n)
# Space Complexity : O(n)