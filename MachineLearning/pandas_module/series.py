import numpy as np
import pandas as pd

labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}

pd.Series(data=my_data)
# 0    10
# 1    20
# 2    30
# dtype: int64

pd.Series(data=my_data,index=labels)
# a    10
# b    20
# c    30
# dtype: int64

pd.Series(arr)
# 0    10
# 1    20
# 2    30
# dtype: int32

pd.Series(data=[sum,print,len])

ser1=pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
ser1

# USA        1
# Germany    2
# USSR       3
# Japan      4
# dtype: int64


