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

