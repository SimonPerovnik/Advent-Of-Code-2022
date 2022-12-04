import numpy as np

# Prvi del

'''
A - rock, B - paper, C - scisors
X - rock, Y - paper, Z - scisors
win - 6, draw - 3, loss - 0
'''


f = open("2\\Data.txt", "r")    

line = f.readline()
score = 0
points = {'X': 1, 'Y': 2, 'Z': 3}
result = {'A X': 3, 'A Y': 6, 'A Z': 0,
          'B X': 0, 'B Y': 3, 'B Z': 6,
          'C X': 6, 'C Y': 0, 'C Z': 3,}
while line:
    line = line[:-1]
    score += points[line[-1]]
    score += result[line]
    line = f.readline()
print(score)

# Drugi del

# X - loss, Y - draw, Z - win

f = open("2\\Data.txt", "r")    

line = f.readline()
score = 0
points = {'X': 0, 'Y': 3, 'Z': 6}
result = {'A X': 3, 'A Y': 1, 'A Z': 2,
          'B X': 1, 'B Y': 2, 'B Z': 3,
          'C X': 2, 'C Y': 3, 'C Z': 1,}
while line:
    line = line[:-1]
    score += points[line[-1]]
    score += result[line]
    line = f.readline()
print(score)


