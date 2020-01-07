#reduce function:
'''
    The reduce(fun,seq) function is used to apply a particular function
    passed in its argument to all of the list elements mentioned in the sequence passed along
    reduce(func,seq)
    reduce() is defined in “functools” module
'''

import functools
lis = [ 1 , 3, 5, 6, 2, ]
#sum of list
print(functools.reduce(lambda a,b:a+b,lis)) #17

#Max of list
print(functools.reduce(lambda a,b:a if a > b else b,lis)) #6

# operator function
import operator

print(functools.reduce(operator.add,lis)) #17

#Max of list
print(functools.reduce(operator.mul,lis)) #180


