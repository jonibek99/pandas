import numpy as np
import pandas as pd
from pandas import DataFrame, Series
obj=Series(np.random.randint(80,size=7),index=['g','f','e','d','c','b','a'])
sort_index=obj.sort_index()
sort_values=obj.sort_values(ascending=False)
# print(sort_index)
print(sort_values)
