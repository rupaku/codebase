'''merge sort
    Merge sort is one of the most efficient sorting algorithms. It works on the
    principle of Divide and Conquer. Merge sort repeatedly breaks down a list into
    several sublists until each sublist consists of a single element and merging those
    sublists in a manner that results into a sorted list.
'''


def mergesort(arr):
    if len(arr) > 1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1
        while i < len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1
        while j < len(R):
            arr[k]=R[j]
            j=j+1
            k=k+1
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")

if __name__ == "__main__":
    arr=[1,4,3,2,5,6]
    mergesort(arr)
    print_list(arr) #1 2 3 4 5 6


#complexity
# all O(nlogn)