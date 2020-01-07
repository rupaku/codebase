''' object
    entity that has state and behaviour
    It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.
'''


''' class
    collection of objects
    logical entity that has some specific attributes and methods.
'''

class A:
    pass
obj=A() #instanciate

#example
class Player:
    def __init__(self,name,age):
        self.name=name
        #attributes ,properties of an object
        self.age=age

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def run(self):
        print('run')
        return 'done'
if __name__ == '__main__':
    Player1 = Player('rupa',25)
    #__ini__ is called when we instantiate this obj
    print(Player1)


''' str and repr
    The print statement and str() built-in function uses __str__ to display 
    the string representation of the object while the repr() built-in function uses __repr__ to display the object.
'''

import datetime
today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))

#Output:

# 2016 - 02 - 22 19: 32:04.078030
# datetime.datetime(2016, 2, 22, 19, 32, 4, 78030)