import numpy as np
import pandas as pd
from pandas import Series,DataFrame
data={
    'age':[10,20,23,34,53,23,3],
    'year':[2020,2023,2025,2026,2027,2028,2029]
}
df=DataFrame(data)
carr=df['age'].corr(df['year'])
print(carr)