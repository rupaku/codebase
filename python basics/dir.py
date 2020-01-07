''' introspection using dir
    attributes and methods that particular instance has
'''

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

print(dir(wizard1)) #attributes and methods under wizard1 instance

#output :sign_in method is also present
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '_
# _gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__
# ', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__
# weakref__', 'attack', 'email', 'name', 'power', 'sign_in']
