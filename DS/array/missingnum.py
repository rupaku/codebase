''' Missing num
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    o/p missing num is 5 in array 2
'''

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1 # missing ele in first array
    return arr1[-1] # last ele of first array

arr1=[1,2,3,4,5,6,7]
arr2=[3,7,2,1,4,6]
print(finder(arr1,arr2)) #5

#method2:
import _collections
def finder(arr1,arr2):
    d=_collections.defaultdict(int)
    for num in arr2: #count of each element in arr2
        d[num]+=1
    for num in arr1: #check that num in arr1
        if d[num] == 0:
            return num
        else:
            d[num]-=1

arr1=[1,2,3,4,5,6,7]
arr2=[3,7,2,1,4,6]
print(finder(arr1,arr2)) #5

#method3
def finder(arr1,arr2):
    res=0
    for num in arr1+arr2: #concatenate two array
        res=res^num
        # print(res)
    return res

arr1=[1,2,3,4,5,6,7]
arr2=[3,7,2,1,4,6]
print(finder(arr1,arr2)) #5