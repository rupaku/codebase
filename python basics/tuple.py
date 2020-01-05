'''
    A Tuple is a collection of Python objects separated by commas.
    In someways a tuple is similar to a list in terms of indexing, nested objects
    and repetition but a tuple is immutable unlike lists which are mutable.
'''
tup1 = ('python', 'geeks')
print(tup1) #('python', 'geeks')
tup2=(1,)

#concatenate
print(tup1 + tup2) #('python', 'geeks', 1)

#Nesting
tup3=(tup1,tup2)
print(tup3) #(('python', 'geeks'), (1,))

#repetition
tup3=('hello',)*3
print(tup3) #('hello', 'hello', 'hello')

#Immutable
tuple1 = (0, 1, 2, 3)
# tuple1[0] = 4
print(tuple1) #typerror 'tuple' object does not support item assignment

#slicing
print(tup1[1:]) #('geeks',)

#Delete a tuple
# del  tup1
print(tup1)

#length
print(len(tup1)) #2

#convert list to tuple
li=[1,2,3]
print(tuple(li)) #(1, 2, 3)

#tuple in loop
for i in range(5):
    tup=('geeks',)
    print(tup,end=" ") #('geeks',) ('geeks',) ('geeks',) ('geeks',) ('geeks',)

#cmp() max() min()

'''reversed
The reversed() function returns the reversed iterator of the given sequence.in tuple ,list,string and range
'''
str='python'
print(list(reversed(str))) # ['n', 'o', 'h', 't', 'y', 'p']

''' sorted
    sorts the elements of a given iterable in a specific order (either ascending or descending).
'''
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list)) #['a', 'e', 'i', 'o', 'u']

''' Zip
    The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
    zip(*iterables)
    - If we do not pass any parameter, zip() returns an empty iterator
    - If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
    - If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.
'''

li1=[1,2,3]
li2=['one','two','three']
print(set(zip(li1,li2))) #{(3, 'three'), (1, 'one'), (2, 'two')}

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')
print(set(zip(numbersList, str_list, numbers_tuple)))   #{(1, 'one', 'ONE'), (2, 'two', 'TWO')}

''' The * operator can be used in conjunction with zip() to unzip the list.

zip(*zippedList)
'''
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
res=list(zip(coordinate,value))
print(res) #[('x', 3), ('y', 4), ('z', 5)]
c,v=zip(*res)
print(c) #('x', 'y', 'z')
print(v)# (3, 4, 5)
