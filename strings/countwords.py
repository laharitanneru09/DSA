#   code to count the number of words in a string
str1 = input("Enter a string: ")

count = 0
in_word = False

for ch in str1:
    if ch not in (" ", ",", "."):
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False

print("The number of words in the string is", count)

# Time Complexity : O(n)
# Space Complexity : O(1)