import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('02_data/test_data', 'r') as casefile:
#     data = casefile.read()
with open ('02_data/full_data', 'r') as casefile:
    data = casefile.read()
startTime = time.time()
count = 0



def check(text):
    spl = 2
    while spl <= len(text):
        if len(text) % spl == 0:
            chunk = 2
            valid = False
            width = int(len(text)/spl)
            while chunk*width <= len(text):
                # print(blue(text[0:width]),yellow(text[(chunk-1)*width:chunk*width]))
                if text[0:width] != text[(chunk-1)*width:chunk*width]:
                    valid = True
                chunk += 1
            if not valid:
                # print(red(text))
                return True
        spl += 1
    # print(green(text))
    return False

lines = data.split(',')

for line in lines:
    i = int(line.split('-')[0])
    end = int(line.split('-')[1])
    while i <= end:
        current = str(i)
        if check(current):
            count += i
        i += 1



print(green("count: " + str(count)))
timerstop(startTime)