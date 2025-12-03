import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('03_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('03_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0


def find(text, first, last):
    biggest = first
    i2 = first
    while i2 < last:
        if int(text[i2]) > int(text[biggest]):
            biggest = i2
        i2 += 1
    return biggest


for bank in lines:
    lastest = -1
    current = ""
    i = -11
    while i <= 0:
        lastest = find(bank, lastest + 1, len(bank) + i)
        current += str(bank[lastest])
        i += 1
    count += int(current)



print(green("count: " + str(count)))
timerstop(startTime)