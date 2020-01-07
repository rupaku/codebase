'''lambda functions
    anonymous function without a name
    which can have any number of arguments, but it can only have one expression.
    doesn't include "return" statement
    don't have to assign it to variable
    application: when we require a nameless function for a short period of time.

    lambda param :action(param)
'''

#cube
def cube(y):
    return y * y * y;

g = lambda x: x * x * x
print(g(7))
print(cube(5))

#example :double
my_list=[1,2,3]
print(list(map(lambda x:x*2,my_list))) #[2, 4, 6]

#example square
print(list(map(lambda x:x**2,my_list))) #[1, 4, 9]

#example list sorting
a=[(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x:x[1])
print(a)

#output
# [(10, -1), (0, 2), (4, 3), (9, 9)]



