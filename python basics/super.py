''' super()
    The super() builtin returns a proxy object (temporary object of the superclass)
    that allows us to access methods of the base class.
    Allows us to avoid using the base class name explicitly
    Working with Multiple Inheritance
'''

class User:
    def __init__(self,email):
        self.email=email
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

# print(wizard1.email) #'Wizard' object has no attribute 'email' without super keyword


####################### NOW with super ######################
class User:
    def __init__(self,email):
        self.email=email
    def sign_in(self):
        print('logged in')
class Wizard(User):
    def __init__(self,name,power, email): #pass email here
        super().__init__(email) #declare super which refers to class above wizard i.e user
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
wizard1=Wizard('rupa',500,'abc@gmail.com') #pass email here

print(wizard1.email) #abc@gmail.com
