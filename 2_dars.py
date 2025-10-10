import numbers as np
import pandas as pd
from pandas import Series
cars_dict={'malibu':122,'nexiya':19000,'lacetti':988313}
# print(type(cars_dict))
cars_pandas=Series(cars_dict)
# print(type(cars_pandas))
# print(cars_pandas)
# p='malibu' in cars_pandas
# print(p)
print(cars_pandas['nexiya'])
models=['yonda','jaguar','nexiya','toyota','laceti','lacetti','mazda','bnw','mer','me','malibu']
cars2=Series(cars_pandas,index=models)
print(cars2)