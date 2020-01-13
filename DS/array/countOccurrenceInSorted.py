def binarySearch(arr,l,r,ele):
    if l <= r:
        mid=int(l+(r-1)/2)
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            return binarySearch(arr,l,mid-1,ele)
        else:
            return binarySearch(arr,mid+1,r,ele)
    else:
        return -1

def countOccurrences(arr, n, x):
    ind = binarySearch(arr, 0, n - 1, x)

    # If element is not present
    if ind == -1:
        return 0

    # Count elements
    # on left side.
    count = 1
    left = ind - 1
    while (left >= 0 and
           arr[left] == x):
        count += 1
        left -= 1

    # Count elements on
    # right side.
    right = ind + 1;
    while (right < n and
           arr[right] == x):
        count += 1
        right += 1

    return count


# Driver code
arr = [1, 2, 2, 2, 2,
       3, 4, 7, 8, 8]
n = len(arr)
x = 2
print(countOccurrences(arr, n, x)) #4