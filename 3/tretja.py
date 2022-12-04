import numpy as np
from string import ascii_letters



# Prvi del

def compare_strings(str1, str2):
    indices = [i in str2 for i in str1 if i in ascii_letters]
    return [str1[i] for i in range(len(str1)) if indices[i]]

f = open("3\\Torba.txt", "r")    

line = f.readline()
score = 0

while line:
    line = line[:-1]
    L = len(line)//2
    char = compare_strings(line[:L], line[L:])[0]
    score += [ord(char) - 96 if char.islower() else ord(char) - 38][0]
    line = f.readline()
print(score)

# Drugi del

f = open("3\\Torba.txt", "r")   

line = f.readline().strip('\n')
score = 0

while line:
    line2 = f.readline().strip('\n')
    line3 = f.readline().strip('\n')
    char = compare_strings(line3, compare_strings(line, line2))[0]
    score += [ord(char) - 96 if char.islower() else ord(char) - 38][0]
    line = f.readline().strip('\n')
print(score)