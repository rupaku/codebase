def findMedianSortedArrays(A, B):
    A.extend(B)
    A.sort()
    n=len(A)
    #odd
    if n % 2 != 0:
        return int(A[int(n / 2)])
    return int((A[int((n - 1) / 2)] +
                A[int(n / 2)]) / 2.0)

A = [1,4,5]
B = [2,3]
print(findMedianSortedArrays(A, B)) #3

