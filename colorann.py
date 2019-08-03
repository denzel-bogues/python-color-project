#import numpy
import pandas as p
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype






data_read = p.read_csv("colors.csv", delimiter = ',', names=['Color names', 'Hex', 'R', 'G', 'B',])
#data_red = data_read[['R', 'G', 'B']]
R = input('Enter red value ')
G = input('Enter greem value ')
B = input('Enter blue value ')

userdata = [R, G, B]
user_df = p.DataFrame(userdata)
in_read = p.DataFrame.transpose(p.DataFrame(user_df))
in_read.columns = ['R', 'G', 'B']

in_read['R'] = in_read['R'].astype(int)
in_read['G'] = in_read['G'].astype(int)
in_read['B'] = in_read['B'].astype(int)



print(in_read)
print(is_string_dtype(in_read['G']))
print(is_numeric_dtype(in_read['G']))
print(p.merge(data_read, in_read, on=['R', 'G', 'B'], how='inner'))


