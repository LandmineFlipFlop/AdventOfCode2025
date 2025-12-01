import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('01_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('01_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0
# setup and data import


dialnum = 50
for turn in lines:
    i = 0
    while i < abs(int(turn)):
        if int(turn) > 0:
            dialnum += 1
        else:
            dialnum -= 1
        dialnum %= 100

        if dialnum == 0:
            count += 1
        i += 1



print(green("count: " + str(count)))
timerstop(startTime)