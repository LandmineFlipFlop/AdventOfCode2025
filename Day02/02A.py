import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('02_data/test_data', 'r') as casefile:
#     data = casefile.read()
with open ('02_data/full_data', 'r') as casefile:
    data = casefile.read()
startTime = time.time()
count = 0
# setup and data import



lines = data.split(',')

for line in lines:
    i = int( line.split('-')[0] )
    end = int( line.split('-')[1] )
    while i <= end:
        current = str(i)
        if len(current) %2 == 0:
            half = int( len(current)/2 )
            if current[ 0 : half ] == current[ half : len(current) ]:
                count += i
        i += 1



print(green("count: " + str(count)))
timerstop(startTime)