'''
A function is called Higher Order Function if it contains other functions
as a parameter or returns a function as an output i.e, the functions that
operate with another function are known as Higher order Functions.
'''

#Function as object
def shout(text):
    return text.upper()
print(shout('hello'))

x=shout
print(x('hello'))

#Passing func as another argument to other functions
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()

def greet(func):
    greeting=func("Hi How are You?")
    print(greeting)
greet(shout)
greet(whisper)

#Returning function
def create_adder(x):
    def adder(y):
        return x+y
    return adder
add=create_adder(15)
print(add(10)) #25