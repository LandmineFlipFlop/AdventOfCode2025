import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('05_data/test_data', 'r') as casefile:
#     data = casefile.read().splitlines()
with open ('05_data/full_data', 'r') as casefile:
    data = casefile.read().splitlines()
startTime = time.time()
count = 0


i = 0
ranges = []
toggle = True
while i < len(data):
    if data[i] == '':
        toggle = False
    else:
        if toggle:
            ranges.append(data[i].split('-'))
            ranges[len(ranges) - 1][0] = int(ranges[len(ranges) - 1][0])
            ranges[len(ranges) - 1][1] = int(ranges[len(ranges) - 1][1])

    i += 1
# data parsing

i = 0
while i < 2000:
    newranges = []
    for range in ranges:
        i2 = 0
        toggle = True
        while i2 < len(newranges):
            if range[0] <= newranges[i2][1] <= range[1]:
                newranges[i2][1] = range[1]
                toggle = False
            if range[0] <= newranges[i2][0] <= range[1]:
                newranges[i2][0] = range[0]
                toggle = False
            if newranges[i2][0] <= range[0] and range[1] <= newranges[i2][1]:
                toggle = False
            i2 += 1
        if toggle:
            newranges.append(range)

    ranges = []
    for newrange in newranges:
        ranges.append(newrange)
    i += 1


for newrange in newranges:
    count += newrange[1] - newrange[0] + 1
    print(newrange, newrange[1] - newrange[0] + 1)

print(green("count: " + str(count)))
timerstop(startTime)