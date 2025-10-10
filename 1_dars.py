import pandas as pd
import numpy as np 
from pandas import Series
obl=Series([1,2,3,4,5,6,7,8,9,'jonibek'])
# print(obl)
# print(obl[9])
obj2=Series([2,3,4,5],index=['ikki','uch','turt','besh'])
# print(obj2[['uch','uch']])
# print(obj2**2)
print(np.exp(obj2))