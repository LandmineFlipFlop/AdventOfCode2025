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
    lines[i] = list(lines[i])
    i += 1

i = 0
longest = 0
while i < len(lines):
    if len(lines[i]) > longest:
        longest = len(lines[i])
    i += 1
# setup

i = 0
while i < len(lines):
    i2 = 0
    while i2 < longest - len(lines[i]) + 1:
        lines[i].append(' ')
        i2 += 1
    i += 1

i = 0
new = []
temp = []
while i < longest:
    i2 = 0
    tally = ''
    while i2 < len(lines) - 1:
        if lines[i2][i] != ' ':
            tally += lines[i2][i]
        i2 += 1
    if tally == '':
        new.append(temp)
        temp = []
    else:
        temp.append(tally)
    i += 1
new.append(temp)

operation = []
for digit in lines[len(lines) - 1]:
    if digit != ' ':
        operation.append(digit)

i = 0
while i < len(new):
    i2 = 0
    if operation[i] == '+':
        summ = 0
    else:
        summ = 1
    while i2 < len(new[i]):
        if operation[i] == '+':
            summ += int(new[i][i2])
        else:
            summ *= int(new[i][i2])
        i2 += 1
    count += summ
    i += 1


print(green("count: " + str(count)))
timerstop(startTime)