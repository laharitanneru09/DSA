# code to compress a string

# Compress a string
# Example: aaabb -> a3b2

text = input("Enter a string: ")

result = ""
count = 1

for i in range(len(text)):
    if i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1

print("Compressed string:", result)

#   Time Complxity : O(n)
#   Space Complexity : (1)