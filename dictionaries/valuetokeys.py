# Find all keys having a given value

dict1 = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

value = int(input("Enter the value to find: "))

keys = []

for key in dict1:
    if dict1[key] == value:
        keys.append(key)

if len(keys) > 0:
    print("Keys having the value", value, "are:", keys)
else:
    print("No key found with the given value")

#   Time Complexity : O(n)
#   Space Complexity : O(n)