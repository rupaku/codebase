''' Polymorphism
     Polymorphism means the ability to take various forms.
     In Python, Polymorphism allows us to define methods in the child class with
     the same name as defined in their parent class.
     As we know, a child class inherits all the methods from the parent class.
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

def player_attack(char):
    char.attack()

player_attack(wizard1) # attacking with power 500  bcz of different object passed

player_attack(archer1) #attacking with power 400


