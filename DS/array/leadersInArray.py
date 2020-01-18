'''
  An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader.
  For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
'''

'''
    Scan all the elements from right to left in an array and keep track of maximum till now. When maximum changes its value, print it.
'''
def leaders(arr):
    size=len(arr)
    max_from_right=arr[size-1]
    print(max_from_right)
    for i in range(size-2,-1,-1):
        if arr[i] > max_from_right:
            print(arr[i])
            max_from_right =arr[i]

arr = [16, 17, 4, 3, 5, 2]
leaders(arr) #2 5 17