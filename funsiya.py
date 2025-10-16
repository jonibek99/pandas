import pandas as pd
import numpy as np
from pandas import Series , DataFrame
df=pd.DataFrame(np.random.randn(3,4),index=list('abc'),columns=['olma','anor','qovun','anjir'])
# print(df.mean(axis=1))
x=lambda i: i+11
apply=df.apply(x)
applymap=df.applymap(lambda I: I**2 )
# print(apply.round())
print(applymap)
