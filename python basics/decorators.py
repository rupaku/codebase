''' decorators
    - Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
    - Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
    - to add functionality to an existing code.
    use:
        Decorators have several use cases such as:
        Authorization in Python frameworks such as Flask and Django
        Logging
        Measuring execution time
        Synchronization
'''

# @gfg_decorator
# def hello():
#     print('hello')

'''
def hello()
    print('hello')

hello=gfg_decorator(hello)

In the above code, gfg_decorator is a callable function, 
will add some code on the top of some another callable function, 
hello_decorator function and return the wrapper function.


'''

#example
def hello_decorator(func):
    def inner(*args,**kwargs):
        print('before execution')
        returned_value=func(*args,**kwargs)
        print('after execution')
        return returned_value
    return inner

@hello_decorator
def sum_two(a,b):
    print('sum')
    return a+b

a,b=1,2
print(sum_two(a,b))

#example:calculate time
from time import time
def performance(func):
    def wrapper_method(*args,**kwargs):
        t1=time()
        res=func(*args,**kwargs)
        t2=time()
        print(f'{t2-t1} s')
        return res
    return wrapper_method


@performance
def calculate_time():
    for i in range(10000000):
        i*5

calculate_time() #0.7599813938140869 s

''' multiple decorators'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

#output
# ['HELLO', 'THERE'] #bottom up approach ist upper then split