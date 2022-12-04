import numpy as np

f = open("1\\Kalorije.txt", "r")    

line = f.readline()
kcal = []
kalor = 0
while line:
    line = line[:-1]
    if line == '':
        kcal.append(kalor)
        kalor = 0
        line = f.readline()
        continue
    kalor += int(line)
    line = f.readline()

print(np.max(kcal))
print(np.sum(np.sort(kcal)[-3:]))
