'''range
    special object that produces a sequence of integers from start(inclusive)
    to stop(exclusive)
    start defaults to 0
    range(4) #0,1,2,3
'''
for i in range(0,5):
    print(i)

#output
# 0
# 1
# 2
# 3
# 4

for _ in range(0,10,2):
    print(_)

#output
# 0
# 2
# 4
# 6
# 8

for _ in range(10,0,-1):
    print(_)
#output
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

for _ in range(10,0,-2):
    print(_)
#output
# 10
# 8
# 6
# 4
# 2
