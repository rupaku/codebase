import pandas as pd

df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                index=[0,1,2,3])

df2=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                index=[4,5,6,7])

df3=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                index=[8,9,10,11])

df1

# A	B	C	D
# 0	A0	B0	C0	D0
# 1	A1	B1	C1	D1
# 2	A2	B2	C2	D2
# 3	A3	B3	C3	D3


df2

# 	A	B	C	D
# 4	A0	B0	C0	D0
# 5	A1	B1	C1	D1
# 6	A2	B2	C2	D2
# 7	A3	B3	C3	D3

df3

# A	B	C	D
# 8	A0	B0	C0	D0
# 9	A1	B1	C1	D1
# 10	A2	B2	C2	D2
# 11	A3	B3	C3	D3

pd.concat([df1,df2,df3])

# A	B	C	D
# 0	A0	B0	C0	D0
# 1	A1	B1	C1	D1
# 2	A2	B2	C2	D2
# 3	A3	B3	C3	D3
# 4	A0	B0	C0	D0
# 5	A1	B1	C1	D1
# 6	A2	B2	C2	D2
# 7	A3	B3	C3	D3
# 8	A0	B0	C0	D0
# 9	A1	B1	C1	D1
# 10	A2	B2	C2	D2
# 11	A3	B3	C3	D3

pd.concat([df1,df2,df3],axis=1) #along column

# A	B	C	D	A	B	C	D	A	B	C	D
# 0	A0	B0	C0	D0	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 1	A1	B1	C1	D1	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	A2	B2	C2	D2	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 3	A3	B3	C3	D3	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 4	NaN	NaN	NaN	NaN	A0	B0	C0	D0	NaN	NaN	NaN	NaN
# 5	NaN	NaN	NaN	NaN	A1	B1	C1	D1	NaN	NaN	NaN	NaN
# 6	NaN	NaN	NaN	NaN	A2	B2	C2	D2	NaN	NaN	NaN	NaN
# 7	NaN	NaN	NaN	NaN	A3	B3	C3	D3	NaN	NaN	NaN	NaN
# 8	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A0	B0	C0	D0
# 9	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A1	B1	C1	D1
# 10	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A2	B2	C2	D2
# 11	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A3	B3	C3	D3



left=pd.DataFrame({'key':['k0','k1','k2','k3'],
                    'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right=pd.DataFrame({'key':['k0','k1','k2','k3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

left

# 	key	A	B
# 0	k0	A0	B0
# 1	k1	A1	B1
# 2	k2	A2	B2
# 3	k3	A3	B3

right

# key	C	D
# 0	k0	C0	D0
# 1	k1	C1	D1
# 2	k2	C2	D2
# 3	k3	C3	D3

pd.merge(left,right,how='inner',on='key')

# 	key	A	B	C	D
# 0	k0	A0	B0	C0	D0
# 1	k1	A1	B1	C1	D1
# 2	k2	A2	B2	C2	D2
# 3	k3	A3	B3	C3	D3


left=pd.DataFrame({'key1':['k0','k0','k1','k2'],
                   'key2':['k0','k1','k0','k1'],
                    'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right=pd.DataFrame({'k0':['k0','k1','k2','k3'],
                    'key2':['k0','k0','k0','k0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

left

# 	key1	key2	A	B
# 0	k0	k0	A0	B0
# 1	k0	k1	A1	B1
# 2	k1	k0	A2	B2
# 3	k2	k1	A3	B3


right

import pandas as pd

df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                index=[0,1,2,3])

df2=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                index=[4,5,6,7])

df3=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                index=[8,9,10,11])

df1

# A	B	C	D
# 0	A0	B0	C0	D0
# 1	A1	B1	C1	D1
# 2	A2	B2	C2	D2
# 3	A3	B3	C3	D3


df2

# 	A	B	C	D
# 4	A0	B0	C0	D0
# 5	A1	B1	C1	D1
# 6	A2	B2	C2	D2
# 7	A3	B3	C3	D3

df3

# A	B	C	D
# 8	A0	B0	C0	D0
# 9	A1	B1	C1	D1
# 10	A2	B2	C2	D2
# 11	A3	B3	C3	D3

pd.concat([df1,df2,df3])

# A	B	C	D
# 0	A0	B0	C0	D0
# 1	A1	B1	C1	D1
# 2	A2	B2	C2	D2
# 3	A3	B3	C3	D3
# 4	A0	B0	C0	D0
# 5	A1	B1	C1	D1
# 6	A2	B2	C2	D2
# 7	A3	B3	C3	D3
# 8	A0	B0	C0	D0
# 9	A1	B1	C1	D1
# 10	A2	B2	C2	D2
# 11	A3	B3	C3	D3

pd.concat([df1,df2,df3],axis=1) #along column

# A	B	C	D	A	B	C	D	A	B	C	D
# 0	A0	B0	C0	D0	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 1	A1	B1	C1	D1	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	A2	B2	C2	D2	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 3	A3	B3	C3	D3	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 4	NaN	NaN	NaN	NaN	A0	B0	C0	D0	NaN	NaN	NaN	NaN
# 5	NaN	NaN	NaN	NaN	A1	B1	C1	D1	NaN	NaN	NaN	NaN
# 6	NaN	NaN	NaN	NaN	A2	B2	C2	D2	NaN	NaN	NaN	NaN
# 7	NaN	NaN	NaN	NaN	A3	B3	C3	D3	NaN	NaN	NaN	NaN
# 8	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A0	B0	C0	D0
# 9	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A1	B1	C1	D1
# 10	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A2	B2	C2	D2
# 11	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	A3	B3	C3	D3



left=pd.DataFrame({'key':['k0','k1','k2','k3'],
                    'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right=pd.DataFrame({'key':['k0','k1','k2','k3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

left

# 	key	A	B
# 0	k0	A0	B0
# 1	k1	A1	B1
# 2	k2	A2	B2
# 3	k3	A3	B3

right

# key	C	D
# 0	k0	C0	D0
# 1	k1	C1	D1
# 2	k2	C2	D2
# 3	k3	C3	D3

pd.merge(left,right,how='inner',on='key')

# 	key	A	B	C	D
# 0	k0	A0	B0	C0	D0
# 1	k1	A1	B1	C1	D1
# 2	k2	A2	B2	C2	D2
# 3	k3	A3	B3	C3	D3


left=pd.DataFrame({'key1':['k0','k0','k1','k2'],
                   'key2':['k0','k1','k0','k1'],
                    'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right=pd.DataFrame({'key1':['k0','k1','k1','k2'],
                        'key2':['k0','k0','k0','k0'],
                             'C':['C0','C1','C2','C3'],
                             'D':['D0','D1','D2','D3']})

left

# 	key1	key2	C	D
# 0	k0	k0	C0	D0
# 1	k1	k0	C1	D1
# 2	k2	k0	C2	D2
# 3	k3	k0	C3	D3


right


# 	key1	key2	C	D
# 0	k0	k0	C0	D0
# 1	k1	k0	C1	D1
# 2	k1	k0	C2	D2
# 3	k2	k0	C3	D3


pd.merge(left,right,on=['key1','key2'])

# key1	key2	A	B	C	D
# 0	k0	k0	A0	B0	C0	D0
# 1	k1	k0	A2	B2	C1	D1
# 2	k1	k0	A2	B2	C2	D2

pd.merge(left,right,how='outer',on=['key1','key2'])

# key1	key2	A	B	C	D
# 0	k0	k0	A0	B0	C0	D0
# 1	k0	k1	A1	B1	NaN	NaN
# 2	k1	k0	A2	B2	C1	D1
# 3	k1	k0	A2	B2	C2	D2
# 4	k2	k1	A3	B3	NaN	NaN
# 5	k2	k0	NaN	NaN	C3	D3

pd.merge(left,right,how='right',on=['key1','key2'])

# 	key1	key2	A	B	C	D
# 0	k0	k0	A0	B0	C0	D0
# 1	k1	k0	A2	B2	C1	D1
# 2	k1	k0	A2	B2	C2	D2
# 3	k2	k0	NaN	NaN	C3	D3


############## Joining ############

#Combine the columns of two potentially differently-indexed data frames into a single dataframe

left=pd.DataFrame({'A':['A0','A1','A2'],
                 'B':['B0','B1','B2']},
                index=['k0','k1','k2'])

right=pd.DataFrame({'C':['C0','C2','C3'],
                 'D':['D0','D2','D3']},
                index=['k0','k2','k3'])

left

# 	A	B
# k0	A0	B0
# k1	A1	B1
# k2	A2	B2

right

# 	C	D
# k0	C0	D0
# k2	C2	D2
# k3	C3	D3

left.join(right)

# A	B	C	D
# k0	A0	B0	C0	D0
# k1	A1	B1	NaN	NaN
# k2	A2	B2	C2	D2

left.join(right,how='outer')

# A	B	C	D
# k0	A0	B0	C0	D0
# k1	A1	B1	NaN	NaN
# k2	A2	B2	C2	D2
# k3	NaN	NaN	C3	D3

