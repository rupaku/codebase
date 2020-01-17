class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        mn, mx = 1, B
        result = []
        for x in A:
            if x == 'D':
                result.append(mx)
                mx -= 1
            elif x == 'I':
                result.append(mn)
                mn += 1
        result.append(mn)
        return result

A=3
B='ID'
obj=Solution()
print(obj.findPerm(A,B))