import numpy as np
import pandas as pd

#Index levels
outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index

# [('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

hier_index=pd.MultiIndex.from_tuples(hier_index)
hier_index

# MultiIndex([('G1', 1),
#             ('G1', 2),
#             ('G1', 3),
#             ('G2', 1),
#             ('G2', 2),
#             ('G2', 3)],
#            )

df=pd.DataFrame(randn(6,2),hier_index,['A','B'])
df


# A	B
# G1	1	-0.497104	-0.754070
# 2	-0.943406	0.484752
# 3	-0.116773	1.901755
# G2	1	0.238127	1.996652
# 2	-0.993263	0.196800
# 3	-1.136645	0.000366

df.loc['G1']

# 	A	B
# 1	1.025984	-0.156598
# 2	-0.031579	0.649826
# 3	2.154846	-0.610259

df.loc['G1'].loc[1] #G1 index 1

# A   -0.925874
# B    1.862864
# Name: 1, dtype: float64

df.index.names
# FrozenList([None, None])

df.index.names=['Groups','num']
df

# 		A	B
# Groups	num
# G1	1	0.641806	-0.905100
# 2	-0.391157	1.028293
# 3	-1.972605	-0.866885
# G2	1	0.720788	-1.223082
# 2	1.606780	-1.115710
# 3	-1.385379	-1.329660

df.loc['G2']

# 	A	B
# num
# 1	0.649148	0.358941
# 2	-1.080471	0.902398
# 3	0.161781	0.833029

df.loc['G2'].loc[2]['B']
# -0.5781202586473068

df.xs('G1')

# A	B
# num
# 1	1.133703	0.528187
# 2	0.393461	-0.630507
# 3	-1.398290	-0.219311

df.xs(1,level='num')

# 	A	B
# Groups
# G1	-0.125381	-0.945588
# G2	0.802129	-1.667537

