# code to find the key with minimum value
dict1={
    "key1":90,
    "key2":8,
    "key3":5,
    "key4":3,
}
min_key="key1"
min_value=dict1[min_key]

for key,value in dict1.items():
    if value<min_value:
        min_value=value
        min_key=key
print("The key with min value is ",min_key)


#   Time Complexity : O(n)
#   Space Complexity : O(1)