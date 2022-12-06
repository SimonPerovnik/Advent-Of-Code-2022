import numpy as np
import re

# Prvi del

f = open("6\\data.txt", "r")

line = f.readline()

buffer = ['p' for i in range(4)]
for index, values in enumerate(line):
    buffer[index % 4] = values
    if len(buffer) == len(set(buffer)):
        print(index+1)
        break

# Drugi del 

f = open("6\\data.txt", "r")

line = f.readline()

buffer = ['p' for i in range(14)]
for index, values in enumerate(line):
    buffer[index % 14] = values
    if len(buffer) == len(set(buffer)):
        print(index+1)
        break
    
    