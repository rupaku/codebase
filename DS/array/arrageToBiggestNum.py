
def comparator(a,b):
    ab=str(a)+str(b)
    ba=str(b)+str(a)
    return ((int(ba) > int(ab)) - (int(ba) < int(ab)))

def mycompare(mycmp):
    class K(object):
        def __init__(self,obj,*args):
            self.obj=obj
        def __lt__(self,other):
            return mycmp(self.obj,other.obj) < 0
        def __gt__(self,other):
            return mycmp(self.obj, other.obj) > 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


if __name__ == "__main__":
    arr = [54, 546, 548, 60, ]
    sorted_Arr=sorted(arr,key=mycompare(comparator))
    num="".join([str(i) for i in sorted_Arr])
    print(num)


#method2
from itertools import permutations
def largeest(arr):
    ls=[]
    for i in permutations(arr,len(arr)):
        ls.append("".join(map(str,i)))
    return max(ls)

#method3
from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        ''' When comparing numbers we must pick the one leading
            to the best concatenated result:
            787978 > 787879  so 7879 is 'bigger' than 78
                        but     7879 is 'less' than 788
        '''

        # Convert to string once, for proper comparison a+b vs b+a
        A = map(str, A)
        key = cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1)
        res = ''.join(sorted(A, key=key, reverse=True))
        # Must left trim 0, apparently
        res = res.lstrip('0')
        return res if res else '0'