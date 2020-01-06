#functions
#math(),print(),max(),min()

'''methods
    python method is called on an object
    A method, then, belongs to a class
'''
#Methods :can be accessed thru .dot
# capitalize() #wrong
'hello'.capitalize()

#__init__() is a magic method that serves as a constructor for the class.
class vehicle:
  def __init__(self,color):
    self.color=color
  def start(self):
    print("Starting engine")
  def showcolor(self):
    print(f"I am {self.color}")
car=vehicle('black') #car is an object
car.start() #start is method

#difference
'''Python method is called on an object, unlike a function. In our example above, 
we call start() on the object ‘car’. Conversely, we call Python function quite generically- 
we don’t call it on any object. Since we call a method on an object, it can access the data within it.
A method may alter an object’s state, but Python function usually only operates on it,
 and then prints something or returns a value.'''