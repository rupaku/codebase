''' frozen set
    Frozensets are like normal sets in every respect except that they cannot be mutated.
    This feature makes them hashable and allows you to use them as items of a set or keys of a dictionary.
'''
#nested set
s = set()
s.add(frozenset((1,2)))
s.add(frozenset((2,3)))
s.add(frozenset((4,5)))
print(s)

#output
{frozenset({4, 5}), frozenset({2, 3}), frozenset({1, 2})}


