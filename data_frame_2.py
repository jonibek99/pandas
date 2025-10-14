from pandas import Series
import pandas as pd
import numpy  as np

uz = {2020: 33.7, 2021: 34.2, 2022: 34.6, 2023: 35.1, 2024: 35.7, 2025: 36.3}
kz = {2020: 18.8, 2021: 19.1, 2022: 19.4, 2023: 19.7, 2024: 20.0, 2025: 20.3}
tj = {2020: 9.5,  2021: 9.8,  2022: 10.0, 2023: 10.3, 2024: 10.6, 2025: 10.9}
tr = {2020: 6.0,  2021: 6.3,  2022: 6.6,  2023: 6.9,  2024: 7.1,  2025: 7.4}
kg = {2020: 6.6,  2021: 6.8,  2022: 7.0,  2023: 7.2,  2024: 7.4,  2025: 7.6}

df=pd.DataFrame({'uzbekistan':uz,
                 'kirgigistan':kz,
                 'tajikistan':tj,
                 'turkmanistan':tr,
                 'kirgistan':kg})
loc=df.loc[2020:2023]>22
iloc=df.iloc[[0,5],[0,3]]
at=df.at[2022,'tajikistan']>df.at[2022,'uzbekistan']
iat=df.iat[1,4]
slicing=pd.Series(np.random.randint(1,99,size=88))
print(slicing.iloc[-1])
# print(loc)
# print(iloc)
# print(at)
# print(iat)