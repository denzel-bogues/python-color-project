import numpy
import pandas as p



data_read = p.read_csv("colors.csv", delimiter = ',', names=['Color names', 'Hex', 'R', 'G', 'B',])
data_read[['R', 'G', 'B']]
R = input('Enter red value')
G = input('Enter greem value')
B = input('Enter blue value')
userdata = [R, G, B]

input_read = p.DataFrame.transpose(p.DataFrame(userdata))

#for index, row in data_read.itterows():