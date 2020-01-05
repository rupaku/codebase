import copy
li1=[1,2,[3,4],5]
print('original copy before deep copy\n')
for i in range(0,len(li1)):
    print(li1[i],end=" ")
li2=copy.deepcopy(li1)
li2[2][0]=6
print('\ncopied list\n')
for i in range(0,len(li2)):
    print(li2[i],end=" ")
print('\noriginal copy after deep copy\n')
for i in range(0,len(li1)):
    print(li1[i],end=" ")

