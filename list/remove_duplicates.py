# code to remove duplicates from a list
list1 = [1,1,2,23,45,65,29,2,3]

new_list = []

for i in list1:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:", new_list)

# Time Complexity : O(n²)
# Space Complexity : O(n)

# Optimised method:
# new_list = list(dict.fromkeys(list1))