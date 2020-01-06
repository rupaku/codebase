import monkeypatching
def monkey_f(self):
    print('monkey_f')

monkeypatching.Myclass.fun=monkey_f
obj=monkeypatching.Myclass()
obj.fun()

#output monkey_f