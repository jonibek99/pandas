from pandas import Series
import pandas as pd
import numpy  as np
data={
    'yil':[2021,2022,2023,2024,2025,2025],
    'aholi':[33,9,34,24.4,232424.3,9],
    'temp':[12,3,123,1232,1313,12321]
}
a=np.arange(1,7)
df=pd.DataFrame(data,index=a,columns=['aholi','temp','yil','yalpi'])
yalpi=pd.Series([18888,32313131,31344665353,87654321,None,33131,9888765])
df.yalpi=yalpi
# print(df)
df['ifli']=df.yalpi>200000
print(df)