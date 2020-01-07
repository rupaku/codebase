''' method resulution order
    In python, method resolution order defines the order in which the base classes are searched
    when executing a method. First, the method or attribute is searched within a class and then
    it follows the order we specified while inheriting.

    - the method resolution order will search the depth-first, then go left to right.
    - To get the method resolution order of a class we can use either
      __mro__ attribute or mro() method.
    - By using these methods we can display the order in which methods are resolved.
'''

class A:
    def rk(self):
        print('A')
class B:
    def rk(self):
        print('B')
class C(A,B):
    def __init__(self):
        print('C')
obj=C()
print(C.__mro__)
print(C.mro())

#output
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


#single inheritance
class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")

r = B()
r.rk()
#output
#In class B

#class B->class A

#Multiple inhertance
class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
class D(B, C):
    pass

r = D()
r.rk()

#output
# In class B
# Class D -> Class B -> Class C -> Class A

#example
class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__)

#output
# (<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)
