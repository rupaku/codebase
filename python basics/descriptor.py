'''
 Python descriptors are created to manage the attributes of different classes which use the object as reference.
 In descriptors we used three different methods that are __getters__(), __setters__(), and __delete__().
 descriptors are referred to as setter and getter, where public functions are used to Get and Set a private variable.
 Python doesn’t have a private variables concept, and descriptor protocol can be considered as a
 Pythonic way to achieve something similar.
'''

class cel:
    def __get__(self,instance,owner):
        return 5*(instance.x-32)/9

    def __set__(self,instance,value):
        instance.x=32+9*value/5

class Temp:
    y=cel()
    def __init__(self,x):
        self.x=x

t=Temp(112)
print(t.y)
t.y=0
print(t.x)

#44.44444444444444
#32.0


###########################################
#Second method
###########################################

class cel:
    def __init__(self,value=0.0):
        self.value=float(value)
    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value=float(value)

class feh:
    def __get__(self,instance,owner):
        return instance.cel*9/5+32
    def __set__(self,instance,value):
        instance.cel=(float(value)-32)*5/9

class temp:
    cel=cel()
    feh=feh()
    print(cel.value)