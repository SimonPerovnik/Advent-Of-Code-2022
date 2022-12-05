import numpy as np
import re


'''
starting configuration:

            [J]             [B] [W]
            [T]     [W] [F] [R] [Z]
        [Q] [M]     [J] [R] [W] [H]
    [F] [L] [P]     [R] [N] [Z] [G]
[F] [M] [S] [Q]     [M] [P] [S] [C]
[L] [V] [R] [V] [W] [P] [C] [P] [J]
[M] [Z] [V] [S] [S] [V] [Q] [H] [M]
[W] [B] [H] [F] [L] [F] [J] [V] [B]
 1   2   3   4   5   6   7   8   9 
'''

def startingConfig():
    # Really messy solution, not optimal, but it does work
    
    Strlist = ['' for i in range(9)]
    for i in range(8):
        indexList = []
        line = f.readline()
        chars = re.findall(r"(?i)\b[a-z]+\b", line)
        for char in chars:
            all = [index for index in range(len(line)) if line.startswith(char, index)] # find all indices
            index = [(i - 2)//4 + 1 for i in all] # calculate correct indices
            index = [i for i  in index if i not in indexList] # chech if we already put an element to any of indices
            indexList.append(index[0])
            Strlist[index[0]] = Strlist[index[0]] + char
    for i in range(9):
        Strlist[i] = Strlist[i][::-1]
    return Strlist

# Prvi del

f = open("5\\data.txt", "r")
config = startingConfig()

line = f.readline()
while line:
    nums = re.findall(r'\d+', line)
    N_occ = int(nums[0])
    N_from = int(nums[1]) - 1
    N_to = int(nums[2]) - 1
    for i in range(N_occ):
        config[N_to] += config[N_from][-1]
        config[N_from] = config[N_from][:-1]
    line = f.readline()
    
result = [stack[-1] for stack in config]
print(''.join(result))

# Drugi del

f = open("5\\data.txt", "r")
config = startingConfig()

line = f.readline()
while line:
    nums = re.findall(r'\d+', line)
    N_occ = int(nums[0])
    N_from = int(nums[1]) - 1
    N_to = int(nums[2]) - 1
    
    config[N_to] += config[N_from][-N_occ:]
    config[N_from] = config[N_from][:-N_occ]
    
    line = f.readline()
    
result = [stack[-1] for stack in config]
print(''.join(result))
