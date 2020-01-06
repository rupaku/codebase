''' check duplicates in list'''
li=[1,2,1,2,14,5,6]
dup=[]
for i in li:
    if li.count(i) >1:
        dup.append(i)
print(dup)

#output
[1,2,1,2]

li=[1,2,1,2,14,5,6]
dup=[]
for i in li:
    if li.count(i) >1:
        if i not in dup:
            dup.append(i)
print(dup)

#output
[1,2]
