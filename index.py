from pandas import Series
import pandas as pd
import numpy  as np

data = {
    'yil': [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028],
    'aholi soni': [34.2, 34.6, 35.1, 35.7, 36.3, 36.8, 37.4, 38.0],  
    'temp': [14.8, 15.1, 15.4, 15.6, 15.9, 16.1, 16.3, 16.5],         
    'zichlik': [75, 76, 77, 79, 80, 82, 83, 85]                     
}

#df=Series(data)
ind=np.arange(1,33)
df=pd.DataFrame(data)
sorted=pd.DataFrame(data).reindex(ind).sort_index()
reindex=df.reindex([7,2,5])
range=df.reindex(index=np.arange(1,33),method='ffill')
colums=df.reindex(ind,columns=['aholi soni','temp']).sort_index()
numpy=np.random.randint(8,size=3)
loc=df.loc[numpy,['yil','aholi soni','zichlik']]
# print(df)
# print(sorted)
#print(reindex)
# print(range)
# print(colums.sample(3))
# print(loc)
# print(numpy)


#-----------------------------------------------------------------
#drop

drop=sorted.drop('yil',axis=1,)
print(drop)