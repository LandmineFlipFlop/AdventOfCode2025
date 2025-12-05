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
ingredients = []
toggle = False
while i < len(data):
    if data[i] == '':
        toggle = True
    else:
        if toggle:
            ingredients.append(data[i])
        else:
            ranges.append(data[i].split('-'))
    i += 1
# data parsing


for ingredient in ingredients:
    toggle = True
    for range in ranges:
        if int(range[0]) <= int(ingredient) <= int(range[1]) and toggle:
            count += 1
            toggle = False


print(green("count: " + str(count)))
timerstop(startTime)