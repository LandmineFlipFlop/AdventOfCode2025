import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('07_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('07_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

lines[0] = lines[0].replace('S', '1')

i = 0
while i < len(lines):
    lines[i] = list(lines[i])
    i += 1

def itteratepos(row,col,itterate):
    if lines[row][col] == '.':
        lines[row][col] = itterate
    else:
        lines[row][col] = str(int(lines[row][col]) + int(itterate))

i = 0
while i < len(lines):
    i2 = 0
    while i2 < len(lines[i]):
        if lines[i][i2] != '.' and lines[i][i2] != '^' and i != len(lines) - 1:
            if lines [i+1][i2] == '^':
                itteratepos(i + 1, i2 - 1, lines[i][i2])
                itteratepos(i + 1, i2 + 1, lines[i][i2])
            else:
                itteratepos(i + 1, i2, lines[i][i2])

        i2 += 1

    i += 1

for num in lines[len(lines) - 1]:
    if num != '.':
        count += int(num)

printmap(lines)

print(green("count: " + str(count)))
timerstop(startTime)