'''filter
    filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
    filter(function, sequence)
    sequence:sets, lists, tuples, or containers of any iterators.
    Returns:  returns an iterator that is already filtered.
    Application: It is normally used with Lambda functions to separate list, tuple, or sets.
'''

my_list=[1,2,3,4]
def odd_only(item):
    return item%2 !=0

print(list(filter(odd_only,my_list))) #[1, 3]
