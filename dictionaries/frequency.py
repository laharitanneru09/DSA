# Count word frequency using a dictionary 
sentence=input("Enter a sentence : ")
words = sentence.split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("Frequencies of each word :")
for word in freq:
    print(word," : ", freq[word])

#Time complexity: O(n)
#Space Complexity:O(n)

#Alternate method:
#for word in words:
#freq[word] = freq.get(word, 0) + 1
#Time Complexity : O(n)
#Space Complexity: O(n)