''' collection module'''

from collections import Counter,defaultdict,OrderedDict

li=[1,2,3,2,3,4,5]
print(Counter(li))

#output
# Counter({2: 2, 3: 2, 1: 1, 4: 1, 5: 1})

#defaultdict
dict=defaultdict(lambda:5,{'a':1,'b':2})
print(dict['c']) #5

#OrderededDict
d=OrderedDict()
d['a']=1
d['b']=2

d2=OrderedDict()
d2['b']=2
d2['a']=1

print(d == d2) #False since orderd is stored

