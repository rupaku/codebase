def linearsearch(arr,ele):
    n=len(arr)
    for i in range(n):
        if arr[i] == ele:
            return i
    return -1

arr=[1,2,3,4,5]
ele=3
result = linearsearch(arr, ele)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result);

#output
# Element is present at index 2

# COMPLEXITY : O(n)

