import numpy as np
import re

# Prvi del

f = open("7\\data.txt", "r")

dirList = []
level = 0

line = f.readline().strip()

while line:
    if line[:3] == 'dir':
        dirList.append(line[4:])
    line = f.readline().strip()

line = f.readline().strip()

while line:
    if line[:3] == 'dir':
        dirList.append(line[4:])
    line = f.readline().strip()


print(dirList)