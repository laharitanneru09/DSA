# Code to find the number of consonants in a string

str1 = input("Enter a string: ")
consonants = 0

for letter in str1:
    if letter.isalpha():         
        if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
            continue
        else:
            consonants += 1

print("Number of consonants:", consonants)

# Time Complexity: O(n)
# Space Complexity: O(1)


#Alternate Method:
# Store vowels in a set for efficient lookup and checks each alphabetic character.
# If the character is not a vowel, it is counted as a consonant.
#Time Complexity: O(n)
#Space Complexity : O(1)