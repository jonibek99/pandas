from pandas import Series
import pandas as pd
import numpy  as np

data = {
    'yil': [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028],
    'aholi soni': [34.2, 34.6, 35.1, 35.7, 36.3, 36.8, 37.4, 38.0],  
    'temp': [14.8, 15.1, 15.4, 15.6, 15.9, 16.1, 16.3, 16.5],         
    'zichlik': [75, 76, 77, 79, 80, 82, 83, 85]                     
}
num=np.random.randint(1,40,size=33)
df=pd.DataFrame(data).reindex(num).sort_index()
obj=Series(np.arange(1,9.),index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(df['aholi soni'])
# obj['a':'c']='king is always king '
print(obj[obj<5])

