#   Code to find the longest string

sentence=input("Enter a sentence : ")

words=sentence.split()

longest=words[0]

for word in words:
    if len(word)>len(longest):
        longest=word
        

print("The longest word in the sentence is ",longest)

#   Time Complexity : O(n)
#   Space Complexity : O(n)