import pandas as pd
import numpy as np
# data frame 1
d1 = {'Customer_id':pd.Series([1,2,3,4,5,6]),
  'Product':pd.Series(['Oven','Oven','Oven','Television','Television','Television'])}
df1 = pd.DataFrame(d1)
# data frame 2
d2 = {'Customer_id':pd.Series([2,4,6]),
    'State':pd.Series(['California','California','Texas'])}
df2 = pd.DataFrame(d2)
#inner join in python pandas
q1 = pd.merge(df1, df2, on='Customer_id', how='inner')
print(q1)
# outer join in python pandas
q2 = pd.merge(df1, df2, on='Customer_id', how='outer')
print(q2)
# left join in python
q3 = pd.merge(df1, df2, on='Customer_id', how='left')
print(q3)
# right join in python pandas
q4 = pd.merge(df1, df2, on='Customer_id', how='right')
print(q4)