import numpy as np
import re

# Prvi del

f = open("8\\data.txt", "r")

line = f.readline().strip()
a = len(line)
trees = np.zeros((a, 99))

# read file
for i in range(99):
    for ind, values in enumerate(line):
        trees[i][ind] = values
    
    line = f.readline().strip()

score = 0

for i in range(99):
    for j in range(99):
        if i==0 or j==0 or j==98 or i==98:
            score +=1
            continue
        if trees[i][j] > np.max(trees[i][:j]) or trees[i][j] > np.max(trees.T[j][:i]) \
        or trees[i][j] > np.max(trees.T[j][i+1:]) or trees[i][j] > np.max(trees[i][j+1:]):
            score += 1

print(score)

# Drugi del

f = open("8\\data.txt", "r")

line = f.readline().strip()
a = len(line)
trees = np.zeros((a, 99))

# read file
for i in range(99):
    for ind, values in enumerate(line):
        trees[i][ind] = values
    
    line = f.readline().strip()

score = []

for i in range(1,98):
    for j in range(1,98):
        result = [0,0,0,0]
        # left
        for k in range(j):
            if trees[i][j-k-1] >= trees[i][j] or (j-k-1) == 0:
                result[0] = k+1
                break
        # right
        for l in range(a-j-1):
            if trees[i][j+l+1] >= trees[i][j] or (j+l+1) == 98:
                result[1] = l+1
                break            
        # down
        for m in range(a-i-1):
            if trees[i+m+1][j] >= trees[i][j] or (i+m+1) == 98:
                result[2] = m+1
                break            
        # up
        for n in range(i):
            if trees[i-n-1][j] >= trees[i][j] or (i-n-1) == 0:
                result[3] = n+1
                break
        score.append(result[0]*result[1]*result[2]*result[3])

print(np.max(score))            