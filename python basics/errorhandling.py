''' Error handling
    :exception
    An exception is an error that happens during execution of a program. When that
    error occurs, Python generate an exception that can be handled, which avoids your
    program to crash.

    The error handling is done through the use of exceptions that are caught in try
    blocks and handled in except blocks. If an error is encountered, a try block
    code execution is stopped and transferred down to the except block.

    The else clause in a try , except statement must follow all except clauses, and is
    useful for code that must be executed if the try clause does not raise an
    exception.

    A finally clause is always executed before leaving the try statement, whether an
    exception has occurred or not.

'''


# try except block
try:
    data = 'something_that_can_go_wrong'

except IOError:
    print('handle_the_exception_error')

else:
    print('doing_different_exception_handling')

#example
while True:
    try:
        age=int(input('enter age'))
        10/age
    except ValueError:
        print('enter a num')
    except ZeroDivisionError:
        print('enter age greater than 0')
    else:
        print('thank you')

#example
def divide(n1,n2):
    try:
        return n1/n2
    except (TypeError , ZeroDivisionError) as err:
        print(err)
def sum(n1,n2):
    try:
        return n1+n2
    except (TypeError , ZeroDivisionError) as err:
        print(err)
print(sum(1,'hello')) #unsupported operand type(s) for +: 'int' and 'str'
print(divide(1,0))

#finally
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# output
# Goodbye, world!
# KeyboardInterrupt