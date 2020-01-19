class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        size = len(A)
        tmpList = [False]*(size)
        for i in range(size):
            if tmpList[int(A[i])]==True:
                return A[i]
            else:
                tmpList[int(A[i])] = True
        return -1

A=[1,2,2,3,4,5,1]
obj=Solution()
print(obj.repeatedNumber(A)) #2