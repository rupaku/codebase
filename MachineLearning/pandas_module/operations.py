import numpy as np
import pandas as pd

df=pd.DataFrame({'col1':[1,2,3,4],
                'col2':[444,555,666,444],
                'col3':['abc','def','ghi','xyz']})

df.head()

# 	col1	col2	col3
# 0	1	444	abc
# 1	2	555	def
# 2	3	666	ghi
# 3	4	444	xyz

df['col2'].unique()

# array([444, 555, 666], dtype=int64)

df['col2'].nunique() #3

df['col2'].value_counts()

# 444    2
# 555    1
# 666    1
# Name: col2, dtype: int64

df

# col1	col2	col3
# 0	1	444	abc
# 1	2	555	def
# 2	3	666	ghi
# 3	4	444	xyz

df[df['col1'] > 2]

# 	col1	col2	col3
# 2	3	666	ghi
# 3	4	444	xyz

df[(df['col1'] > 2) & (df['col2'] == 444)]

# 	col1	col2	col3
# 3	4	444	xyz

df['col1']>2

# 0    False
# 1    False
# 2     True
# 3     True
# Name: col1, dtype: bool

def times2(x):
    return x*2

df['col1']

# 0    1
# 1    2
# 2    3
# 3    4
# Name: col1, dtype: int64

df['col1'].sum() #10

df['col1'].apply(times2)

# 0    2
# 1    4
# 2    6
# 3    8
# Name: col1, dtype: int64

df['col1'].apply(lambda x:x*2)

# 0    2
# 1    4
# 2    6
# 3    8
# Name: col1, dtype: int64

df.drop('col1',axis=1,inplace=True)

df.columns

# Index(['col2', 'col3'], dtype='object')

df.index

# RangeIndex(start=0, stop=4, step=1)

df.sort_values('col2')

# 	col2	col3
# 0	444	abc
# 3	444	xyz
# 1	555	def
# 2	666	ghi

df.isnull()


# col2	col3
# 0	False	False
# 1	False	False
# 2	False	False
# 3	False	False


data={'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
     'C':['x','y','x','y','x','y'],
     'D':[1,3,2,5,4,1]}

df=pd.DataFrame(data)
df


# A	B	C	D
# 0	foo	one	x	1
# 1	foo	one	y	3
# 2	foo	two	x	2
# 3	bar	two	y	5
# 4	bar	one	x	4
# 5	bar	one	y	1

df.pivot_table()
df.pivot_table(values='D',index=['A','B'],columns=['C'])