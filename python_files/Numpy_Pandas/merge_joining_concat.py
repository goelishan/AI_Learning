# Merging
# Joining
# Concatenation

import pandas as pd

df1=pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})

df2=pd.DataFrame({'ID':[4,5,6],'Name':['D','E','F']})

result=pd.concat([df1,df2])

print(result)

df3 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df4 = pd.DataFrame({'ID': [1, 2, 4], 'Salary': [1000, 2000, 3000]})


merged=pd.merge(df3,df4,on='ID',how='inner')
print(merged)

