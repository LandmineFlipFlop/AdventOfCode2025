import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
with open ('06_data/test_data', 'r') as casefile:
    lines = casefile.read().splitlines()
# with open ('06_data/full_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
startTime = time.time()
count = 0

i = 0
while i < len(lines):
    line = lines[i].split(' ')
    tally = ''
    new = []
    for num in line:
        if num == '':
            tally += '0'
        elif num == '+' or num == '*':
            pass
        else:
            tally += num
            new.append(tally)
            tally = ''
        print(new)
    line = new
    lines[i] = line
    i += 1

# data import
print(lines)
i = 0

while i < len(lines[0]):
    i += 1


print(green("count: " + str(count)))
timerstop(startTime)