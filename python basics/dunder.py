''' dunder methods
    Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. 
    Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading.
    Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
'''

class Toy:
    def __init__(self,color,age):
        self.color=color
        self.age=age
        self.mydict={
            'name':'yoyo',
            'has_pets':False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted')

    def __call__(self):
        return('yes')

    def __getitem__(self,i):
        return self.mydict[i]

obj=Toy('red',0)
print(obj.__str__()) #red
print(len(obj)) #5
# del obj #deleted
print((obj())) #yes
print(obj['name']) #yoyo
