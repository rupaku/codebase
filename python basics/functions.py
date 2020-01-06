''' function :block of code which gets executed when called
'''

#parameters:varaibles we receive when we define our function
def say_hello(name,age):
    print(f'hello {name} {age}')

#default parameters : even if we forget to pass arguments while calling it will work.
def say_hello(name='ram',age=20):
    print(f'hello {name} {age}')

say_hello() #called without arguments  hello ram 20

#arguments-actual values we pass while calling our function
#positional arguments:position of value matters
say_hello('rupa',24)

#keyword arguments :increases readebility
say_hello(age=24,name='rupa')

''' return 
    function should return something
'''
def sum_of_num(num1,num2):
    return num1+num2
total=sum_of_num(10,20)
print(total) #30

