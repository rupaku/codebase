'''docstring
    documentation string to maintain readability of code,document it
    to add comments and definition to function
'''

def test(a):
    ''' test method'''
    print(a)
help(test) #help function to get docstring of function test

#output
# test(a)
#     test method

print(test.__doc__) #magic method   test method