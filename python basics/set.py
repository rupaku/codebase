'''SET:
   A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
'''
my_set={1,2,3,4,5}
your_set={4,5,6,7,8,9,10}
demo_set ={4,5}


print(my_set.discard(5))                  # None
print(my_set)                             # {1, 2, 3, 4}
print(my_set.difference_update(your_set)) # None
print(my_set)                             # {1, 2, 3, 4}
print(my_set.add(11))                     # NOne
print(my_set)                             # {1, 2, 3, 4, 5, 11}
print(my_set.union(your_set))             # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} can be user |
print(my_set.intersection(your_set))      # {4, 5}   can be used &
print(my_set.difference(your_set))        # {1, 2, 3}
print(my_set.clear())
print(my_set.isdisjoint(your_set))        # anything in common true else false o/p False
print(demo_set.issubset(your_set))        # True
print(your_set.issuperset(demo_set))      # True
print(del(my_set))                        # delete whole set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)       #removes common and print both set

print(z)                            #{"google", "microsoft", "banana", "cherry"}

x.symmetric_difference_update(y)    #{"google", "microsoft", "banana", "cherry"} #update it

print(x)

fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)            # {"apple", "banana", "cherry"}