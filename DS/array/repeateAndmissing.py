def repeatedNumber(arr):
    arr = list(arr)
    size = len(arr)
    output = []
    for i in range(size):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            output.append(abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            output.append(i + 1)
    return output

arr=[1,2,3,5,6,2]
print(repeatedNumber(arr)) #[2,4] [repeating,missing]