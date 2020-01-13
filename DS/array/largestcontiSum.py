''' largest continuous sum

'''

def large_conti_sum(arr):
    if len(arr) == 0:
        return
    max_sum=current_sum=arr[0]
    for num in arr[1:]:
        current_sum=max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)
    return max_sum

arr=[1,2,-1,3,4,10,10,-10,-1]
print(large_conti_sum(arr)) #29
#

#non negative sum array
def longestSubarry(arr, n):
    res = 0
    for i in range(n):
        curr_count = 0
        while (i < n and arr[i] >= 0):
            curr_count += 1
            i += 1
        res = max(res, curr_count)
    return res

arr=[1, 2, 5, 7, 2, 3]
print(longestSubarry(arr))
