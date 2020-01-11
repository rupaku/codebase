''' coroutines
    subroutines:
    When the logic of a complex function is divided into several self-contained steps
    that are themselves functions, then these functions are called helper functions or subroutines.

    coroutines:
    Coroutines are generalization of subroutines. They are used for cooperative multitasking
    where a process voluntarily yield (give away) control periodically or when idle in order
    to enable multiple applications to be run simultaneously.

    thread vs coroutine:
    In case of threads, it’s operating system (or run time environment) that switches
    between threads according to the scheduler. While in case of coroutine, it’s the
    programmer and programming language which decides when to switch coroutines.
'''

#creating coroutines
def searching(string):
    print("searching string {}".format(string))
    while True:
        name=(yield)
        if string in name:
            print(name)

x=searching("rupa")
x.__next__()
x.send("rupa")
x.send("hello")

#output
# searching string rupa
# rupa
