'''
conda install sqlalchemy
conda install lxml
conda install html5lib
conda install BeautifulSoup4

'''

import pandas as pd

df=pd.read_csv('example.csv')

df.to_csv('My_output',index=False) #not want to save index num

pd.read_excel('Excel_sample.xlsx',sheetname='Sheet1')

df.to_excel('Excel_sample2.xlsx',sheet_name='NewSheet')

data=pd.read_html('https://www.fdic.gov/banklist.html')

type(data) #list

data[0].head()

from sqlalchemy import create_engine

engine=create_engine('sqlite:///:memory:')

df.to_sql('my_table',engine)

sqldf=pd.read_sql('my_table',con=engine)

sqldf


