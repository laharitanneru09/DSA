#code to invert/swap the keys and values in dictionary
dict={"n1":2007,"n2":2008,"n3":2009,"n4":2010}
swapped={}

for key in dict:
    swapped[dict[key]]=key

print("Original Dictionary:", dict)
print("Inverted Dictionary:", swapped)

# Time Complexity: O(n)
# Space Complexity: O(n)


#Alternate method
#inverted = {value: key for key, value in d.items()}