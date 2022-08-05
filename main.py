import numpy as np
import pandas as pd

with open('glove.6B.50d.txt', 'r') as file:
    data = file.readlines()

# No clue why this exists -> forgot to document it
for i in range(len(data)):
    data[i] = data[i][:-1]

# Add all codes to a dictionary
data_dict = dict()

for i in range(len(data)):

    split_data = data[i].split()
    data_dict[split_data[0]] = np.array(split_data[1:]).astype('float64')

# Convert string to norm
def norm(s):
    np.sqrt(np.sum((data_dict[s]**2)))
