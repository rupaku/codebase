'''
closure: A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
USE: As closures are used as callback functions,
    they provide some sort of data hiding.
    This helps us to reduce the use of global variables.
    When we have few functions in our code, closures prove to be efficient way.
    But if we need to have many functions, then go for class (OOP).

'''

def outer(text):
    text=text
    def inner():
        print(text)
    return inner  #Note we are returning function WITHOUT parenthesis
myfunc=outer('hey')
myfunc()

#second example
import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger=logger(add)
add_logger(3,3)

#output
#6