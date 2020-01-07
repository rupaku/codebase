''' abstraction
    Abstraction is used to hide internal details and show only functionalities
    done using public and private variables using _ in front of variable.
'''

print([1,2,3,1].count(1)) #no need to know how count func works we just call

#example
class Player:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def speak(self):
        print(f'My name is {self._name} and age is {self._age}')
Player1=Player('rupa',25)
Player1.speak() #My name is rupa and age is 25

