import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('03_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('03_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

for bank in lines:
    stored = 0
    i = 0
    while i < len(bank):
        i2 = len(bank) - 1
        while i2 > i:
            if  ( int(bank[i])*10 ) + int(bank[i2]) > stored:
                stored = ( int(bank[i])*10 ) + int(bank[i2])
            i2 -= 1
        i += 1
    # print(yellow(bank), green(stored))
    count += stored



print(green("count: " + str(count)))
timerstop(startTime)