'''enumerate
    Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
    This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
    enumerate(iterable, start=0)
    Parameters:
    Iterable: any object that supports iteration
    Start: the index value from which the counter is 
           to be started, by default it is 0 
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
