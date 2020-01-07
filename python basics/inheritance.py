''' inhertance
    By using inheritance, we can create a class which uses all the properties and behavior of another class.
    The new class is known as a derived class or child class, and the one whose properties are acquired is
    known as a base class or parent class.

    It provides re-usability of the code.
'''

class User:
    def sign_in(self):
        print('logged in')
class Wizard(User):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(f'attacking with power {self.power}')
class Archer(User):
    def __init__(self,name,num_of_arrows):
        self.name=name
        self.num_of_arrows=num_of_arrows
    def attack(self):
        print(f'attacking with power {self.num_of_arrows}')
wizard1=Wizard('rupa',500)
archer1=Archer('ram',400)
wizard1.attack()
archer1.attack()

#output
# attacking with power 500
# attacking with power 400

''' isinstance
    returns whether an object is an instance of a class or subclass
    '''
print(isinstance(wizard1,Wizard)) #True since wizard1 obj is instance of class Wizard
print(isinstance(wizard1,User)) #True since it is subclass of User
print(isinstance(wizard1,object)) #True base class is object