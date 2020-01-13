def duplicates(arr):
    ls=[]
    for i in arr:
        if i not in ls:
            ls.append(i)
    return ls

arr=[1,2,2,4,5]
print(duplicates(arr)) #[1, 2, 4, 5]
