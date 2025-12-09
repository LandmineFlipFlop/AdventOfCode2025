import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('09_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('09_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0



i = 0
while i < len(lines):
    lines[i] = lines[i].split(',')
    lines[i][0] = int(lines[i][0])
    lines[i][1] = int(lines[i][1])
    i += 1

for coord1 in lines:
    for coord2 in lines:
        size =abs( (coord2[0] - coord1[0]) + 1) * abs( (coord2[1] - coord1[1]) + 1)
        if  size > count:
            count = size


print(green("count: " + str(count)))
timerstop(startTime)