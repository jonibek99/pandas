
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Ikkita Series yaratamiz
a = Series(np.arange(1,8), index=['a','b','c','d','e','f','g'])
b = Series(np.random.randint(1,8,7), index=['a','c','d','b','f','e','g'])

# Ikkita DataFrame yaratamiz
dfn1 = DataFrame(np.arange(12.).reshape(3,4), columns=['a','b','c','d'], index=['olma','banan','uzum'])
dfn2 = DataFrame(np.arange(12.).reshape(4,3), columns=['c','b','a'], index=['olma','banan','uzum','mandarin'])
sub=dfn2.sub(dfn1,fill_value=0)
# # Serieslarni qo‘shish
# qushuv = a + b
# q=dfn1.T+dfn2.T
# print(q)
# print(dfn1.add(dfn1,fill_value=0).T)
print(sub)