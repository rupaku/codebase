'''iterable
    object or collection of items that can be iterated eg. list ,tuple,string,dict,set
    iterarted:one by one check each item in collection
    '''

user={
    'name':'rupa',
    'work':'engineer',
    'place':'patna'
}
for item in user.items():
    print(item)

#output
# ('name', 'rupa')
# ('work', 'engineer')
# ('place', 'patna')
