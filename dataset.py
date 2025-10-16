import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame({
    'olma':   [10, 20, 10, 40, 30],
    'anor':   [5, 5, 7, 8, 9],
    'banan':  [100, 120, 100, 80, 70],
    'gilos':  [3, 9, 6, 6, 12]
}, index=np.arange(1, 6))   

print(df['olma'].argsort())
