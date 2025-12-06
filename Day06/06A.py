import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('06_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('06_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

i = 0
while i < len(lines):
    line = lines[i].split(' ')
    while '' in line:
        line.remove('')
    lines[i] = line

    i += 1

# data import
print(lines)
i = 0

while i < len(lines[0]):
    if lines[len(lines) - 1][i] == '+':
        sum = 0
    else:
        sum = 1
    i2 = 0
    while i2 < len(lines) - 1:
        if lines[len(lines) - 1][i] == '+':
            sum += int(lines[i2][i])
        else:
            sum *= int(lines[i2][i])
        i2 += 1

    count += sum
    i += 1


print(green("count: " + str(count)))
timerstop(startTime)