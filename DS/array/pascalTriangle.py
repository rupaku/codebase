'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
'''


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1, r):
                row.append(result[r - 1][i - 1] + result[r - 1][i])
            row.append(1)
            result.append(row)
        return result


obj = Solution()
print(obj.generate(5))

