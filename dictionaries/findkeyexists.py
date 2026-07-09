#finding if a given key exists in the dictionary
# Method 1 : Using 'in' operator
# Time Complexity: O(1) average case, O(n) worst case
# Space Complexity: O(1)
student={
    "name":"Lahari",
    "age":18,
    "branch":"CSE"
}
key = input("Enter the key to search: ")

if key in student:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")

# Alternative Method:
# Iterate through all keys using a loop.
# Time Complexity: O(n)
# Space Complexity: O(1)