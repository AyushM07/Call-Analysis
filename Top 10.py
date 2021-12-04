import csv 
import pandas as pd 
df= pd.read_csv('/Users/AyushMadhogaria/Desktop/311_Service_Requests_2020.csv')
df=df.loc[df['Incident Zip']==10027]
df
