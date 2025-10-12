import numpy
from pandas import Series
import pandas
cars_dict={'malibu':122,'nexiya':19000,'lacetti':988313}
car1 = Series({'malibu': 99999, 'laceti': 9323232})
models=['yonda','jaguar','nexiya','toyota','laceti','lacetti','mazda','bnw','mer','me','malibu']
cars2=Series(cars_dict,index=models)
car3 = Series({'laceti': 99999, 'malibu': 9323232})
#MEthods
# print(cars2.isnull())
print(car3+car1)



