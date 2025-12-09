import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
with open ('08_data/test_data', 'r') as casefile:
    lines = casefile.read().splitlines()
length = 10
# with open ('08_data/full_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
# length = 1000
startTime = time.time()
count = 0

i = 0
while i < len(lines):
    lines[i] = lines[i].split(',')
    i2 = 0
    while i2 < len(lines[i]):
        lines[i][i2] = int(lines[i][i2])
        i2 += 1
    i += 1

def dist(x1,y1,z1,x2,y2,z2):
    return int(math.sqrt(  ( (x2 - x1)*(x2 - x1) ) + ( (y2 - y1)*(y2 - y1) ) + ( (z2 - z1)*(z2 - z1) )  ))


def sorter(e):
    return e[1]

dists = []
def isinlist(inlist):
    for item in dists:
        if item[0] == inlist or item[0] == [inlist[1],inlist[0]]:
            return False
    return True


for line1 in lines:
    for line2 in lines:
        if line1 != line2 and isinlist([line1,line2]):
            dists.append([[line1,line2],dist(line1[0],line1[1],line1[2],line2[0],line2[1],line2[2])])

dists.sort(key=sorter)


print(green("count: " + str(count)))
timerstop(startTime)