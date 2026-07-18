# Program to merge two dictionaries without using built-in functions

dictionary1 = {"n1":101, "n2":102, "n3":103}
dictionary2 = {"s1name":"Rina", "s2name":"Tina", "s3name":"Lina"}

merged = {}

# Add elements of the first dictionary
for key in dictionary1:
    merged[key] = dictionary1[key]

# Add elements of the second dictionary
for key in dictionary2:
    merged[key] = dictionary2[key]

print("Merged Dictionary:", merged)

# n = number of elements in dictionary1
# m = number of elements in dictionary2
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

# Alternate method (without built-in functions):
# Add all key-value pairs from dictionary2 directly into dictionary1.
# Time Complexity: O(m)
# Extra Space Complexity: O(1)
# This modifies the original dictionary1.