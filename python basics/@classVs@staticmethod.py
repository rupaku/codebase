'''
Class method vs Static Method

A class method takes cls as first parameter while a static method needs no specific parameters.
A class method can access or modify class state while a static method can’t access or modify it.
In general, static methods know nothing about class state. They are utility type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
When to use what?

We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.

'''

class Player:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def run(self):
        print('run')
        return 'done'
    @classmethod
    def add(cls,num1,num2): #cls for class methods
        return num1 +num2

    @staticmethod
    def add2(num1,num2): #no cls
        return num1+num2
if __name__ == '__main__':
    Player1 = Player('rupa',25) #instantiate
    print(Player1.add(10,20)) #30
    #without instantiate we can call class methods
    print(Player.add(10, 20))  # 30
    print(Player.add2(30,40)) #70
