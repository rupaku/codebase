''' if found return 1 else 0'''
def search(mat,ele):
    n=len(mat)
    i=0
    j=n-1
    while i < n and j >= 0:
        if mat[i][j] == ele:
            return 1
        elif mat[i][j] > ele:
            j=j-1
        else:
            i=i+1
    return 0

A = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
B = 3
print(search(A,B)) #1

#method2 using binary search
def searchMatrix(self, mat, ele):
    n = len(mat)
    for i in range(n):
        start = 0
        end = len(mat[i]) - 1
        while start <= end:
            mid = (start + end) // 2
            if mat[i][mid] == ele:
                # break
                return 1
            elif ele < mat[i][mid]:
                end = mid - 1
            else:
                start = mid + 1

    return 0

