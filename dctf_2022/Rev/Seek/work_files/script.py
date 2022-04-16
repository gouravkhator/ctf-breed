import numpy as np
import pandas as pd

data = pd.read_csv("character_positions.csv")

maximum = -1

# finding maximum position so that we can build the string from the characters and position given
for index, row in data.iterrows():
    position = np.int64(row['position']) # convert numpy int64 to native python int class
    character = np.int64(row['char'])
    
    maximum = max(maximum, position)

res = ['']*(maximum+1)

for index, row in data.iterrows():
    position = np.int64(row['position'])
    character = np.int64(row['char'])

    res[position] = chr(character) # convert ASCII to character

flag = "".join(res) # convert array of characters to string

print(flag)
