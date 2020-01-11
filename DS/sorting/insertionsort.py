''' insertion sort'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
arr=[1,4,5,7,2]
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")

#output
# 1 2 4 5 7

#complexity
# worst: O(n2) when reversed
# best: O(n) when all same element
# average : O(n2)
