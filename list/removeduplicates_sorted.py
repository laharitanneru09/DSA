# Remove duplicates from a sorted list (In-place)

lst = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]

if len(lst) == 0:
    print("List is empty")
else:
    j = 0

    for i in range(1, len(lst)):
        if lst[i] != lst[j]:
            j += 1
            lst[j] = lst[i]

    print("Original List =", lst)

    print("After Removing Duplicates = ", end="")

    print("[", end="")
    for i in range(j + 1):
        print(lst[i], end="")
        if i != j:
            print(", ", end="")
    print("]")

# Time Complexity : O(n)
# Space Complexity : O(1)