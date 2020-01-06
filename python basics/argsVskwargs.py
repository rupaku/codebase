''' *args
    can accept any num of positional arguments
    returns tuple
'''

def func(*args):
    print(*args)
    return sum(args)
print(func(1,2,3,4))

#output
# 1 2 3 4
# 10

''' **kwargs
    any num of keyword aruments
    return dictionary
'''
def func(*args,**kwargs):
    total=0
    for items in kwargs.values():
        total=total+items
    return sum(args) + total
print(func(1,2,3,4,num1=5,num2=10))

#output
# 25

#example
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

#output
# arg1: Geeks
# arg2: for
# arg3: Geeks


kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

#output
# arg1: Geeks
# arg2: for
# arg3: Geeks
#
