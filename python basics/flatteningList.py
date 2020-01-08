''' Flattening List
    Converting a list of lists (2D), into a list (1D) is called flattening.
'''

#Nested loop
list_2d=[[1,2,3],[4,5,6],[7,8,9]]
list_flat=[]
for i in range(len(list_2d)):
    for j in range(len(list_2d[i])):
        list_flat.append(list_2d[i][j])
print('original list',list_2d)
print('flattened list',list_flat)

#output
# original list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened list [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Functools
import functools
import operator
list_2d=[[1,2,3],[4,5,6],[7,8,9]]
list_flat=functools.reduce(operator.iconcat,list_2d,[])
print('original list',list_2d)
print('flattened list',list_flat)

#itertools
import itertools
list_2d=[[1,2,3],[4,5,6],[7,8,9]]
list_flat=list(itertools.chain(*list_2d))
print('original list',list_2d)
print('flattened list',list_flat)