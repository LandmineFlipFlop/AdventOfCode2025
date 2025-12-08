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
        lines[i][i2] = float(lines[i][i2])
        i2 += 1
    i += 1

def dist(x1,y1,z1,x2,y2,z2):
    return math.sqrt(  ( (x2 - x1)*(x2 - x1) ) + ( (y2 - y1)*(y2 - y1) ) + ( (z2 - z1)*(z2 - z1) )  )

shortpath = []
def findshortest():
    lowest = 999999999999.0
    lowpos1 = []
    lowpos2 = []
    for line1 in lines:
        for line2 in lines:
            if line1 != line2:
                if dist(line1[0],line1[1],line1[2],line2[0],line2[1],line2[2]) < lowest:
                    if not ([lowpos1,lowpos2] in shortpath or [lowpos2,lowpos1] in shortpath):
                        lowest = dist(line1[0],line1[1],line1[2],line2[0],line2[1],line2[2])
                        lowpos1 = line1
                        lowpos2 = line2
    shortpath.append([lowpos1,lowpos2])
    print(green(lowest), shortpath)

i = 0
while i < 4:
    findshortest()
    i += 1

print(green("count: " + str(count)))
timerstop(startTime)