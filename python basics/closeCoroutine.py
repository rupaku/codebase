def searching(string):
    print("searching string {}".format(string))
    try:
        while True:
            name=(yield)
            if string in name:
                print(name)
    except GeneratorExit:
        print("closing the coroutine")

x=searching("rupa")
x.__next__()
x.send("rupa")
x.send("rupa")
x.close()

#output
# searching string rupa
# rupa
# rupa
# closing the coroutine
