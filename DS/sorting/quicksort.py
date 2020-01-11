'''quick sort'''
def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low < high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

if __name__ == "__main__":
    arr=[4,3,1,6,7]
    n=len(arr)
    quick_sort(arr,0,n-1)
    for i in range(n):
        print(arr[i],end=" ") #1 3 4 6 7

#complexity
# worst:O(n2) #when pivot is greatest or smallest
# best:O(nlogn) #when pivot is middle
# average:(O(nlogn))
