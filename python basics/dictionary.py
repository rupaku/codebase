'''
    Dictionary in Python is an unordered collection of data values, used to store data values like a map,
    Dictionary holds key:value pair
    Keys of a Dictionary must be unique and of immutable data type such as Strings, Integers and tuples,
    but the key-values can be repeated and be of any type.
'''
dic={1:'geeks',2:'for',3:'geeks'}
print(dic) #{1: 'geeks', 2: 'for', 3: 'geeks'}

Dict = dict([(1, 'Geeks'), (2, 'For')])
print(Dict) #{1: 'Geeks', 2: 'For'}

#nested dictionary
Dict={1:'geeks',2:{3:'for',4:'geeks'}}
print(Dict) #{1: 'geeks', 2: {3: 'for', 4: 'geeks'}}

#add element
Dict={}
Dict[0]='geeks'
Dict[1]='for'
Dict[2]='geeks'
print(Dict) #{0: 'geeks', 1: 'for', 2: 'geeks'}

#Update values of keys
Dict[2]='Hello'
print(Dict) #{0: 'geeks', 1: 'for', 2: 'Hello'}

#access elements
print(Dict[1]) #for
#using get
print(Dict.get(2)) #hello

#delete dic:deletion of keys can be done by using the del keyword
# del Dict[1]
print(Dict)

# Clear:All the items from a dictionary can be deleted at once by using clear() method.
# Dict.clear()
# Dict.pop(2)
#Deleting an arbitrary Key-value pair
# Dict.popitem()

#keys
print(Dict.keys()) #dict_keys([0, 1, 2])

#values
print(Dict.values()) #dict_values(['geeks', 'for', 'Hello'])

#items
print(Dict.items()) #dict_items([(0, 'geeks'), (1, 'for'), (2, 'Hello')])

#update
Dict1={1:'A'}
Dict2={2:'B'}
Dict1.update(Dict2)
print(Dict1) #{1: 'A', 2: 'B'}

Dict1.update(B = 'For', C = 'Geeks')
print(Dict1) #{1: 'A', 2: 'B', 'B': 'For', 'C': 'Geeks'}

#setdefault
#returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.

Dict1.setdefault('D', 'Geeks')
print(Dict1['D']) #Geeks

#has_keys
# returns true if specified key is present in the dictionary, else returns false.
print(Dict1)
# print(Dict1.has_key('B'))

#fromkeys()
# generate a dictionary from the given keys.
#Syntax : fromkeys(seq, val)

seq = { 'a', 'b', 'c', 'd', 'e' }
res=dict.fromkeys(seq,1)
print(res) #{'a': 1, 'c': 1, 'd': 1, 'e': 1, 'b': 1}


