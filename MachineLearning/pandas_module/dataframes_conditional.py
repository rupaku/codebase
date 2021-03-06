import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df

booldf=df>0
booldf

# 	W	X	Y	Z
# A	True	True	True	True
# B	True	False	False	True
# C	False	True	True	False
# D	True	False	False	True
# E	True	True	True	True

df[booldf]

# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	NaN	NaN	0.605965
# C	NaN	0.740122	0.528813	NaN
# D	0.188695	NaN	NaN	0.955057
# E	0.190794	1.978757	2.605967	0.683509

df['W'] > 0
# A     True
# B     True
# C    False
# D     True
# E     True
# Name: W, dtype: bool

df[df['W']>0]

# 	W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509

res=df[df['W']>0]
res

# 	W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509

res['X']
# A    0.628133
# B   -0.319318
# D   -0.758872
# E    1.978757
# Name: X, dtype: float64

res[['Y','X']]
# 	Y	X
# A	0.907969	0.628133
# B	-0.848077	-0.319318
# D	-0.933237	-0.758872
# E	2.605967	1.978757

boolser=df['W']>0
result=df[boolser]
mycols=['Y','X']
result[mycols]


# Y	X
# A	0.907969	0.628133
# B	-0.848077	-0.319318
# D	-0.933237	-0.758872
# E	2.605967	1.978757

df[(df['W']>0) & (df['Y']>1)]

# 	W	X	Y	Z
# E	0.190794	1.978757	2.605967	0.683509

df[(df['W']>0) | (df['Y']>1)]


# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509

df.reset_index()
# 	index	W	X	Y	Z
# 0	A	2.706850	0.628133	0.907969	0.503826
# 1	B	0.651118	-0.319318	-0.848077	0.605965
# 2	C	-2.018168	0.740122	0.528813	-0.589001
# 3	D	0.188695	-0.758872	-0.933237	0.955057
# 4	E	0.190794	1.978757	2.605967	0.683509

newind='CA NY WY OR CO'.split()
newind

# ['CA', 'NY', 'WY', 'OR', 'CO']

df['States']=newind
df

# W	X	Y	Z	States
# A	2.706850	0.628133	0.907969	0.503826	CA
# B	0.651118	-0.319318	-0.848077	0.605965	NY
# C	-2.018168	0.740122	0.528813	-0.589001	WY
# D	0.188695	-0.758872	-0.933237	0.955057	OR
# E	0.190794	1.978757	2.605967	0.683509	CO

df.set_index('States',inplace=True) #set states col as index

# 	W	X	Y	Z
# States
# CA	2.706850	0.628133	0.907969	0.503826
# NY	0.651118	-0.319318	-0.848077	0.605965
# WY	-2.018168	0.740122	0.528813	-0.589001
# OR	0.188695	-0.758872	-0.933237	0.955057
# CO	0.190794	1.978757	2.605967	0.683509

df
