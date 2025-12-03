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
    while i < len(bank) - 12:
        i2 = len(bank) - 11
        while i2 > i:
            i3 = len(bank) - 10
            while i3 > i2:
                i4 = len(bank) - 9
                while i4 > i3:
                    i5 = len(bank) - 8
                    while i5 > i4:
                        i6 = len(bank) - 7
                        while i6 > i5:
                            i7 = len(bank) - 6
                            while i7 > i6:
                                i8 = len(bank) - 5
                                while i8 > i7:
                                    i9 = len(bank) - 4
                                    while i9 > i8:
                                        i10 = len(bank) - 3
                                        while i10 > i9:
                                            i11 = len(bank) - 2
                                            while i11 > i10:
                                                i12 = len(bank) - 1
                                                while i12 > i11:
                                                    test = (int(bank[i]) * 100000000000) + (int(bank[i2]) * 10000000000) + (int(bank[i3]) * 1000000000) + (int(bank[i4]) * 100000000) + (int(bank[i5]) * 10000000) + (int(bank[i6]) * 1000000) + (int(bank[i7]) * 100000) + (int(bank[i8]) * 10000) + (int(bank[i9]) * 1000) + (int(bank[i10]) * 100) + (int(bank[i11]) * 10) + int(bank[i12])
                                                    if test > stored:
                                                        stored = test
                                                    i12 -= 1
                                                i11 -= 1
                                            i10 -= 1
                                        i9 -= 1
                                    i8 -= 1
                                i7 -= 1
                            i6 -= 1
                        i5 -= 1
                    i4 -= 1
                i3 -= 1
            i2 -= 1
        i += 1
    # print(yellow(bank), green(stored))
    count += stored



print(green("count: " + str(count)))
timerstop(startTime)