import numpy as np
import re

# Prvi del

f = open("4\\data.txt", "r")    

line = f.readline()
score = 0
while line:
    nums = [int(s) for s in re.findall(r'\d+', line)]   # Get all integers from string
    if (nums[0] - nums[2]) * (nums[1] - nums[3]) <= 0:  # Condition for complete overlapping 
        score += 1
    line  = f.readline()
    
print(score)
 
# Drugi del

f = open("4\\data.txt", "r")    

line = f.readline()
score = 0
while line:
    nums = [int(s) for s in re.findall(r'\d+', line)]   # Get all integers from string
    if list(set(range(nums[0], nums[1]+1)) & set(range(nums[2], nums[3]+1))):  # Condition for any overlapping 
        score += 1
    line  = f.readline()
    
print(score)
