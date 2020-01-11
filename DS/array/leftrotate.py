
def leftrotatebyone(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
def leftrotate(arr,d,n):
    for i in range(d):
        leftrotatebyone(arr,n)
arr = [1, 2, 3, 4, 5, 6, 7]
leftrotate(arr, 2, 7)
for i in range(len(arr)):
    print(arr[i],end=" ") #3 4 5 6 7 1 2

