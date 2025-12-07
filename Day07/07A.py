import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('07_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('07_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

lines[0] = lines[0].replace('S', '|')

i = 0
while i < len(lines):
    lines[i] = list(lines[i])
    i += 1

i = 0
while i < len(lines):
    i2 = 0
    while i2 < len(lines[i]):
        if lines[i][i2] == '|' and i != len(lines) - 1:
            if lines [i+1][i2] == '^':
                count += 1
                lines[i + 1][i2-1] = '|'
                lines[i + 1][i2 + 1] = '|'
            else:
                lines[i + 1][i2] = '|'

        i2 += 1
    printmap(lines)
    print(green('---------------'))

    i += 1

print(lines)

print(green("count: " + str(count)))
timerstop(startTime)