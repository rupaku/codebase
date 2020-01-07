''' set comprehension
'''

mylist={i for i in 'hello'}
print(mylist) #{'h', 'l', 'e', 'o'}

''' Dictionary comprehension

'''

sample_dict={
    'a':1,
    'b':2
}
my_dict={k:v for k,v in sample_dict.items()}
print(my_dict) #{'a': 1, 'b': 2}

my_dict={k:v*2 for k,v in sample_dict.items()}
print(my_dict) #{'a': 2, 'b': 4}

my_dict={k:v*2 for k,v in sample_dict.items() if v%2 ==0}
print(my_dict) #{'b': 4}

#example
my_dict={num:num*2 for num in [1,2,3]}
print(my_dict) #{1: 2, 2: 4, 3: 6}

#duplicates using list comprehension

demo_list=['a','a','b','c','c']
dup=list(set([x for x in demo_list if demo_list.count(x) > 1]))
print(dup)

#output
#['a', 'c']

