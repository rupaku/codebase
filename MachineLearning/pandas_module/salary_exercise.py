import pandas as pd

sal=pd.read_csv('Salary.csv')

sal.head()

sal.head(2)

sal.info()

#avg base pay
sal['BasePay'].mean()

#highest amt of overtimepay in dataset
sal['OverTimePay'].max()

#job title of JOSEPH DRISCOLL
sal[sal['EmployeeName']] == 'JOSEPH DRISCOLL']['JobTitle']

#how much joseph driscoll make including benefits
sal[sal['EmployeeName']] == 'JOSEPH DRISCOLL']['JobTitle']['TotalPayBenefits']

#name of highest paid person including benefits
sal[sal['TotalPayBenefits'] == sal['TotalPayABenefits'].max()]['EmployeeName']

#name of lowest paid person

sal[sal['TotalPayBenefits'] == sal['TotalPayABenefits'].min()]['EmployeeName']

#avg base pay of all employees per year
sal.groupby('Year').mean()['BasePay']


#unique job titles are there?
sal['JobTitle'].nunique

#top 5 most common jobs
sal['JobTitle'].value_counts().head()

#job title with only one occurence in 2013
sum(sal['Year'] == 2013]['JobTitle'].value_counts() ==1)

#how many ppl have word chief in their job title
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False
sum(sal['JobTitle'].apply(lambda x:chief_string(x)))

#is there any corelation btwn length of job totle string and salary
sal['totle_len']=sal['JobTitle'].apply(len)
sal['TotalPayBenefits','title_len']].corr()







