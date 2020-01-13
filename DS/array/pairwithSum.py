def printPairs(arr, arr_size, sm):
    s = set()
    for i in range(0, arr_size):
        temp = sm - arr[i]
        if temp in s:
            print("Pair with given sum " + str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")"+s.add(arr[i]))

A = [1, 4, 45, 6, 10, 8]
sm = 16
printPairs(A, len(A), sm)

#output
# Pair with given sum 16 is (10, 6)