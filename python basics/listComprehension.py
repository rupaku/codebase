''' List comprehension
    List comprehension is an elegant way to define and create list in Python.
    These lists have often the qualities of sets, but are not in all cases sets.
    List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce().
'''

#without comprehension
my_list=[]
for i in 'hello':
    my_list.append(i)
print(my_list) #['h', 'e', 'l', 'l', 'o']


#with comprehension
my_list=[i for i in 'hello']
print(my_list) #['h', 'e', 'l', 'l', 'o']

my_list=[ i for i in range(0,10) if i%2 == 0]
print(my_list) #[0, 2, 4, 6, 8]

my_list=[ i**2 for i in range(0,10) if i%2 == 0]
print(my_list) #[0, 4, 16, 36, 64]
