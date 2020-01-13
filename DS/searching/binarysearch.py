def binarysearch(arr,l,r,ele):
    if l <= r:
        mid=int(l+(r-1)/2)
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            return binarysearch(arr,l,mid-1,ele)
        else:
            return binarysearch(arr,mid+1,r,ele)
    else:
        return -1


arr=[1,2,3,5,6,7]
ele=6
res=binarysearch(arr,0,len(arr),ele)
if res != -1:
    print("Element is present at index % d" % res)
else:
    print("Element is not present in array")

#output
# Element is present at index  4

# complexity: O(logn)
