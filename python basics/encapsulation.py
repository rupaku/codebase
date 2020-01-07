''' encapsulation
     It is used to restrict access to methods and variables.
     code and data are wrapped together within a single unit from being modified by accident.
'''
class Player:
    def __init__(self,name,age):
        self.name=name
        #attributes ,properties of an object
        self.age=age

if __name__ == '__main__':
    Player1 = Player('rupa',25)
    #__ini__ is called when we instantiate this obj
    print(Player1.name) #rupa

#wrapped whole as an object and can access all its methods as a unit
'hello'.capitalize() #after . we can access any methods of string object