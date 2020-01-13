def firstMissingPositive(arr):
    arr = set(arr)
    for i in range(1, len(arr) + 2):
        if i not in arr:
            return i

arr=[1,2,4,5,6]
print(firstMissingPositive(arr)) #3