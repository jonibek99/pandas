from pandas import Series
import pandas as pd
import numpy  as np
data={
    'uzbekistan':{2021:33,2021:23,2023:212,2024:43},
    'kazakhdan':{
        2021:11,
        2022:13,
        2023:45,
        2024:54,
    }
}
df=pd.DataFrame(data)
df.index.name='yillar'
arr=df.values
#print(df.T)
print(arr)