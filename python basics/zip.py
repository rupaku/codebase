''' Zip
    The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
    zip(*iterables)
    - If we do not pass any parameter, zip() returns an empty iterator
    - If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
    - If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.
'''

my_list=[1,2,3]
your_list=[4,5,6]

print(list(zip(my_list,your_list)))

#output
# [(1, 4), (2, 5), (3, 6)]
