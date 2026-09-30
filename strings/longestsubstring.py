# Find the longest substring without repeating characters
# Optimized using sliding window

string = input("Enter a string: ")

last_seen = {}
start = 0
longest = 0

for i in range(len(string)):

    if string[i] in last_seen and last_seen[string[i]] >= start:
        start = last_seen[string[i]] + 1

    last_seen[string[i]] = i

    current_length = i - start + 1

    if current_length > longest:
        longest = current_length

print("Length of longest substring:", longest)

#   Time complexity : O(n)
#   Space Complexity : O(n)