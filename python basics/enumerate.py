'''enumerate
   adds counter to iterable
 '''

for i,char in enumerate('hello'):
    print(i,char)

#output
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o

for i,char in enumerate([1,2,3]):
    print(i,char)

#output
# 0 1
# 1 2
# 2 3

for i,char in enumerate(list(range(10))):
    if char == 50:
        print(f'index of 50 is {i}')

#index of 50 is 50