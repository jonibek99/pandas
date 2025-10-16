import numpy as np
import pandas as pd
from pandas import Series , DataFrame
df1=DataFrame(np.arange(9.).reshape(3,3),columns=list('bcd'),index=['olma','anor','uzum'])
df2=DataFrame(np.arange(12.).reshape(4,3),columns=list('abc'),index=['olma','anor','qovun','anjir'])
add1=df1.add(df1,fill_value=0)
add2=df2.add(df1,fill_value=0)
sub1=df1.sub(df2,fill_value=1)
sub2=df2.sub(df1,fill_value=0)
rsub1=df1.rsub(df2,fill_value=11)
rsub2=df2.rsub(df1,fill_value=11)
# qushuv=df1+df2
# print(qushuv)
# print(df1)
# print(df2)
# print(add1)
#print(add2.T)
# print(sub1)
# print(sub2.T)
# print(rsub1)
print(rsub2)