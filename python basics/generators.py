'''  Generators
    - generate sequence of value over time
    - range is generator

    Generator-Function :
    - A generator-function is defined like a normal function, but whenever it needs to generate a value,
     it does so with the yield keyword rather than return. If the body of a def contains yield,
     the function automatically becomes a generator function.

    Generator-Object :
    - Generator functions return a generator object. Generator objects are used either by calling
      the next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).

    - Generators are used to create iterators, but with a different approach.
    - Generators are simple functions which return an iterable set of items, one at a time, in a special way.

'''

#example 1
def simple_generator():
    yield 1
    yield 2
    yield 3
for i in simple_generator():
    print(i)

#output
# 1
# 2
# 3

#example 2
def simple_generator():
    yield 1
    yield 2
    yield 3
x= simple_generator()
print(x.__next__()) #1
print(x.__next__()) #2
print(x.__next__()) #3

''' generator application
    Iterators don’t compute the value of each item when instantiated. 
    They only compute it when you ask for it. This is known as lazy evaluation.

    Lazy evaluation is useful when you have a very large data set to compute. 
    It allows you to start using the data immediately, while the whole data set is being computed.
'''

#fibonacci using generator
def fibo(limit):
    a,b=0,1
    while a < limit:
        yield a
        a,b=b,a+b
x=fibo(5)
print(x.__next__()) #0
print(x.__next__()) #1
print(x.__next__()) #1
print(x.__next__()) #2
print(x.__next__()) #3
print(x.__next__()) #stop iteration

#using loop
print("Using for in loop")
for i in fibo(5):
    print(i, end=' ')

#output
# Using for in loop
# 0 1 1 2 3
