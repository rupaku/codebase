'''bubble sort
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
'''
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for  j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[6,5,2,1,8]
bubble_sort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ") #1 2 5 6 8

#complexity
# best:O(n)
# worst:O(n2)
# avg :O(n2)

