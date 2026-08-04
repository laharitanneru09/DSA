#code to remove duplicates from a string
str1=input("Enter a string : ")


visited = {}
result = ""

for ch in str1:
    if ch not in visited:
        visited[ch] = 1
        result += ch

print(result)
for ch in str1:
    if ch not in str2


#Time complexity : O(n)
#Space Complexity : O(n)