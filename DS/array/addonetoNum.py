'''
If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
'''

def plusOne(A):
    s=""
    ls=[]
    for i in A:
        s=s+str(i)

    sum=int(s)+1
    sum_str=str(sum)
    for i in sum_str:
        ls.append(int(i))
    return ls

A=[0]
print(plusOne(A))


#solution
def plusOne(self, A):
    val = 1;
    for i in range(len(A), 0, -1):
        val = val + A[i - 1]
        borrow = int(val / 10)
        if borrow == 0:
            A[i - 1] = val
            break;
        else:
            A[i - 1] = val % 10
            val = borrow
    A = [borrow] + A
    while A[0] == 0:
        del A[0]
    return A