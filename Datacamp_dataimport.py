import pickle
import pandas as pd
import xlrd
from sas7bdat import SAS7BDAT
import matplotlib.pyplot as plt
import scipy.io
from sqlalchemy import create_engine
from urllib.request import urlretrieve
file = r"C:\Users\Adrian\Documents\Data_Journalism\Datacamp \
    Lesson Datafiles\PRIO Battle Deaths Dataset.xls"
xl = pd.ExcelFile(file)
print(xl.sheet_names)

df = xl.parse('bdonly')
print(df.head())

with SAS7BDAT('C:/Users/Adrian/Documents/Data_Journalism/DataCamp\
 Lesson Datafiles/sales.sas7bdat') as file1:
    df_sas = file1.to_data_frame()

print(df_sas.head())
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
mat = scipy.io.loadmat('C:/Users/Adrian/Documents/Data Journalism/DataCamp\
 Examples/ja_data1.mat')
print(type(mat))
engine = create_engine('C:/Users/Adrian/Documents/Data Journalism/DataCamp \
Examples/sqlite:///Chinook.sqlite')
table_names = engine.table_names()
print(table_names)
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_\
1606/datasets/winequality-red.csv'

urlretrieve(url, 'C:/Users/Adrian/Documents/Data Journalism/DataCamp\
 Examples/winequality-red.csv')
df1 = pd.read_csv('C:/Users/Adrian/Documents/Data Journalism/DataCamp\
 Examples/winequality-red.csv', sep=';')
print(df1.head())
df2 = pd.read_csv(url, sep=';')
print(df2.head())
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

url2 = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data\
_into_r/latitude.xls'
xl1 = pd.read_excel(url2, sheetname=None)
print(xl1.keys())
print(xl1['1700'].head())
