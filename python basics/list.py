'''
    List is a collection which is ordered and changeable. Allows duplicate members.
'''

List = []
List.append(1)
List.append('Geeks')
List.append('for')
List.append('Geeks')
List.insert(1,'Hello')
List.extend(['Goodbye','people'])
print(List)
print(List[1])
print(List[-1])
print(List[:])
print(List[::1])
print(List[::2])
List.remove('for')
print(List)
List.pop()
print(List)
List.pop(0)
print(List)
print(List[1:4])
print(List[::-1])

list2 = ['cat', 'bat', 'mat', 'cat',
         'get', 'cat', 'sat', 'pet']
print(list2.index('cat'))  # 0
print(list2.index('cat', 2, 6 )) # ele,start,end # 3
print(list2.count('cat')) #3

# To get the number of occurrences
# of each item in a list
print([[i,list2.count(i)] for i in set(list2)])

# To get the number of occurrences
# of each item in a dictionary
print(dict((i,list2.count(i))for i in set(list2)))

numbers = [1, 3, 4, 2]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#Example for Key sort
def sortSecond(val):
    return val[1]

list1 = [(1, 2), (3, 3), (1, 1)]
list1.sort(key=sortSecond)
print(list1)

list1.sort(key=sortSecond, reverse=True)
print(list1)

#reduce function:
'''The reduce(fun,seq) function is used to apply a particular function
passed in its argument to all of the list elements mentioned in the sequence passed along'''

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

''' accumulate:
    apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
    Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. 
    reduce() is defined in “functools” module, accumulate() in “itertools” module.
    reduce(fun,seq)
    accumulate(seq,fun) 
'''

import itertools

#sum of list
print(list(itertools.accumulate(lis,lambda a,b:a+b))) #[1, 4, 9, 15, 17]

''' sum function'''
print(sum(lis)) #17

''' ord function returns unicode of character'''
print(ord('a')) #97
# print(ord('ab')) #error only one character

'''chr function returns a string for unicode integer'''
print(chr(97)) #a
print(chr(400)) #UnicodeEncodeError: 'ascii' codec can't encode character

'''cmp :compares two list elements
   Syntax : cmp(list1, list2)
   Returns : This function returns 1, if first list is “greater” than second list,
   -1 if first list is smaller than the second list
    else it returns 0 if both the lists are equal.
'''
list1 = [ 1, 2, 4, 3]
list2 = [ 1, 2, 5, 8]


# print cmp(list2, list1)  used in python2
#max() min()

#length of list
print(len(lis))

'''Any (like or)
   Returns true if any of the items is True. It returns False if empty or all are false.
'''
print (any([False, True, False, False])) #True
print(any([False, False, False, False]))  #False

'''All (like and)
   Returns true if all of the items are True
'''
print (all([True, True, True, True])) #True
print (all([False, True, True, False])) #False

'''enumerate
    Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
    This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
    enumerate(iterable, start=0)
    Parameters:
    Iterable: any object that supports iteration
    Start: the index value from which the counter is 
           to be started, by default it is 0 
'''
l1=["eat","sleep","dance"]
obj=enumerate(l1)
print(list(enumerate(l1)))  #[(0, 'eat'), (1, 'sleep'), (2, 'dance')]
print(list(enumerate(l1,2))) #start index

#in loop
for ele in enumerate(l1):
    print(ele)

'''filter
    filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
    filter(function, sequence)
    sequence:sets, lists, tuples, or containers of any iterators.
    Returns:  returns an iterator that is already filtered.  
    Application: It is normally used with Lambda functions to separate list, tuple, or sets.  
    '''
seq = [0, 1, 2, 3, 5, 8, 13]
# result contains even numbers of the list
res=filter(lambda x:x%2 == 0,seq)   #[0, 2, 8]
print(list(res))

'''map
   returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
   map(fun, iter)
   fun : It is a function to which map passes each element of given iterable.
   iter : It is a iterable which is to be mapped.
    '''

#addition
def add(n):
    return n+n
num=(1,2,3,4)
res=map(add,num)
print(list(res)) #[2, 4, 6, 8]

#using map
print(list(map(lambda x:x+x,num)))  #[2, 4, 6, 8]

#add two list using lambda and map
num1=[1,2,3]
num2=[4,5,6]
print(list(map(lambda x,y:x+y,num1,num2))) #[5, 7, 9]

#list of string
l = ['sat', 'bat', 'cat', 'mat']
print(list(map(list,l)))        #[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]

'''lambda functions
    anonymous function without a name
    which can have any number of arguments, but it can only have one expression.
    doesn't include "return" statement
    don't have to assign it to variable
    application: when we require a nameless function for a short period of time.
'''
#cube
def cube(y):
    return y * y * y;

g = lambda x: x * x * x
print(g(7))
print(cube(5))

#lambda with filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print(list(filter(lambda x: (x%2!=0),li))) #[5, 7, 97, 77, 23, 73, 61] odd

#lambda with map
print(list(map(lambda x:x*2,li))) #[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

#lambda with reduce
#sum of list
from functools import reduce
print(reduce(lambda x,y:x+y,li)) #481

