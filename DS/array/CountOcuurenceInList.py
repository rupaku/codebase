'''
Lets say, user provides a list as:

    ['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1']


Your function should return:

    {
      "python": 2,
      "pyhton3": 1,
      "user1": 2,
      "assignment": 1,
      "user": 1,
      "User1":1
    }
'''
count={}
n=int(input("no of elements"))
arr = list(map(str, input("elements list").strip().split()))[:n]
print(arr)
for i in arr:
    if i in count:
        count[i] = count[i]+1
    else:
        count[i] =1
print(count)
