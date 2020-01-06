print(True == 1) #True
print('' == 1) #False
print([] == 1) #False
print(10 == 10.0) #True
print([] == []) #True
print('1' == 1) #False different types

''' is operator hecks for value in memory'''
print(True is 1) #False
print(True is True) #True
print([] is []) #False for datastructure like list it allocates new location every time
print([1,2,3] is [1,2,3]) #False for datastructure like list it allocates new location every time
print([1,2,3] == [1,2,3]) #True checks for its equality of value