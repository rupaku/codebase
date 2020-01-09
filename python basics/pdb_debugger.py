'''pdb debugger'''

import pdb
def add(num1,num2):
    pdb.set_trace() #Python stops and waits for you to tell it what to do next.
    return num1+num2

add(1,'abc')

#commands
# step :to step over next line
# continue : Continue execution and only stop when a breakpoint is encountered.
# b breakpoint b 11 (breakpoint num)
# a:to give all arguments4
# w:context of current line
#exit:  q :to exit out of code
#list : list all code lines
# p filename print filename
#w where : to print stack trace
#n :next line “step over”.
#s step "step into"
# n (next)	Continue execution until the next line in the current function is reached or it returns.
# s (step)	Execute the current line and stop at the first possible occasion (either in a function that is called or in the current function).
#display :Display the value of expression if it changed, each time execution stops in the current frame.
