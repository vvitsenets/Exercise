import pandas as pd 
import numpy as np
from matplotlib import pyplot
from pandas import read_csv, DataFrame, Series
data = pd.read_csv('/Users/macbookpro/Desktop/study/DataAnalysis/House Price.csv')
print(data)
data = data.drop(['recroom','fullbase','gashw','airco','prefarea'],axis=1)
print(data)

#!!!!
#TheFirst - DataFrame +
df = pd.DataFrame(data)
print(data)
#data.price[data.price.isnull()] = data.price.mean()

#testhist
data.pivot_table('count', 'garagepl', 'price', 'count').plot(kind='bar', stacked=True)
fig, axes = pyplot.subplots(ncols=2)
data.pivot_table('count', ['bedrooms'], 'price', 'count').plot(ax=axes[0], title='SibSp')
data.pivot_table('count', ['bathrms'], 'price', 'count').plot(ax=axes[1], title='Parch')
m1 = data.price[data.lotsize.notnull()].count()
print(m1)
#data.Age = data.Age.median()
#endtesthist

#preproc
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
dicts = {}

label.fit(data.driveway.drop_duplicates()) #задаем список значений для кодирования
dicts['driveway'] = list(label.classes_)
data.driveway = label.transform(data.driveway) #заменяем значения из списка кодами закодированных элементов 
#endpreproc

pyplot.hist(data['price'])
pyplot.show()
desc = data["price"].describe() 
print(desc)

pricesum = sum(data['price'])
print(pricesum)


df1 = pd.DataFrame({'first': ['auto', 'cardriver', 'music', 'comfort'],'mark': [1, 2, 3, 5]})
print(df1)
df2 = pd.DataFrame({'second': ['auto', 'cardriver', 'music', 'comfort'],'mark': [5, 0, 7, 8]})
print(df2)
#df2.cardriver[df2.cardriver.isnull()] = df2.cardriver.mean()
finish = df1.merge(df2, left_on='first', right_on='second')

print(finish)


export_csv = finish.to_csv (r'/Users/macbookpro/Desktop/finish.csv', index = None, header=True) 



