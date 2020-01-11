def x(sentence,next_coroutine):
    y=sentence.split(" ")
    for z in y:
        next_coroutine.send(z)
    next_coroutine.close()

def u(pattern="rupa",next_coroutine=None):
    print("searching pattern {}".format(pattern))
    try:
        while True:
            z=(yield)
            if pattern in z:
                next_coroutine.send(z)
    except GeneratorExit:
        print("done with matching process")

def printing():
    try:
        while True:
            z=(yield)
            print(z)
    except GeneratorExit:
        print("done with pipelining")

d=printing()
d.__next__()
f=u(next_coroutine=d)
f.__next__()

sentence="my name is rupa"
x(sentence,f)

#output
# searching pattern rupa
# rupa
# done with matching process
# done with pipelining
