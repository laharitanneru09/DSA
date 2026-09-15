# Find the first non-repeating character

str = input("Enter a string: ")

count = {}

# Count frequency of each character
for chr in str:
    if chr in count:
        count[chr] += 1
    else:
        count[chr] = 1

# Find the first character with frequency 1
for chr in str:
    if count[chr] == 1:
        print("First non-repeating character:", chr)
        break

# Time complexity: O(n)
# Space complexity: O(n)