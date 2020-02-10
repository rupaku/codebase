import pandas as pd
df=pd.read_csv('hrdata.csv',
               index_col='name',
               parse_dates=['hire date'],
               header=0)
print(df)

#writing
df.loc['cookie cat']=['2016-07-04',2000,0]
df.to_csv('hrdata_modified.csv')