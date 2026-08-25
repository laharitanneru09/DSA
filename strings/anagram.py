#  Code to check whether the given strings are anagrams

def is_anagram(s, t):
    frequency = {}

    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    for ch in t:
        if ch not in frequency:
            return False
        frequency[ch] -= 1

    for value in frequency.values():
        if value != 0:
            return False

    return True


s = input("Enter first string: ")
t = input("Enter second string: ")

if is_anagram(s, t):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#   Time Complexity : O(n+m) where n is length of s and m is length of t
#   Space Complexity : O(k) where k is the number of distinct characters