import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
with open ('06_data/test_data', 'r') as casefile:
    lines = casefile.read().splitlines()
# with open ('06_data/full_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
startTime = time.time()
count = 0





print(green("count: " + str(count)))
timerstop(startTime)