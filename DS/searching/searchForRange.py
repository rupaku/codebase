
'''
Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]
'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers

    def searchRange(self, A, B):
        low = 0
        high = len(A) - 1
        res = -1
        while (low <= high):
            mid = (low + high) // 2
            if (A[mid] == B):
                res = mid
                high = mid - 1
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        x = res
        low = 0
        high = len(A) - 1
        res= -1
        while (low <= high):
            mid = (low + high) // 2
            if (A[mid] == B):
                res = mid
                low = mid + 1
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        y = res
        return [x, y]


obj=Solution()
A = [5, 17, 100, 111]
B = 3
print(obj.searchRange(A,B))