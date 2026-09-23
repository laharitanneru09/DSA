# Check whether two dictionaries are equal

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2, "c": 3}

if len(dict1) != len(dict2):
    print("Dictionaries are not equal")
else:
    equal = True

    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            equal = False
            break

    if equal:
        print("Dictionaries are equal")
    else:
        print("Dictionaries are not equal")

#   Time complexity : O(n)
#   Space complexity : O(1)