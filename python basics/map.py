''' Map
   returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
   map(fun, iter)
   fun : It is a function to which map passes each element of given iterable.
   iter : It is a iterable which is to be mapped.

   map(func,*iterables)
'''

my_list=[1,2,3]
def multiply(item):
    return item*2

print(list(map(multiply,my_list))) #[2, 4, 6]
