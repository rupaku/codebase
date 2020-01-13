def findMean(a, n):
    sum = 0
    for i in range(0, n):
        sum += a[i]

    return float(sum / n)

a = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
n = len(a)
print("Mean =", findMean(a, n)) #Mean = 4.5
