import numpy as np
import matplotlib.pyplot as plt

# Prvi del

def check1(cycle):
    if ((cycle - 20) % 40) == 0 or cycle == 20:
        score.append(X*cycle)    
    return None
f = open("10\\data.txt", "r")

line = f.readline().strip()

cycle = 1
X = 1
score = []

while line:
    if line[:4] == 'noop':
        cycle += 1
        check1(cycle)
    if line[:4] == 'addx':
        cycle += 1
        check1(cycle)
        cycle += 1
        X += int(line[5:])
        check1(cycle)
        
    line = f.readline().strip()

print(np.sum(score))

# Drugi del

def check2(cycle, X):
    if abs((cycle % 40) - X) < 2:
        CRT[int(cycle // 40)][cycle % 40 ] = 1
    return None

f = open("10\\data.txt", "r")

line = f.readline().strip()

CRT = np.zeros((6,40))
cycle = 0
X = 1
score = []

while line:
    check2(cycle, X)
    if line[:4] == 'noop':
        cycle += 1
        check2(cycle, X)
    if line[:4] == 'addx':
        cycle += 1
        check2(cycle, X)
        cycle += 1
        X += int(line[5:])
        check2(cycle, X)

    line = f.readline().strip()

plt.imshow(CRT)
plt.show()