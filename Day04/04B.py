import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('04_data/test_data', 'r') as casefile:
#     grid = casefile.read().splitlines()
with open ('04_data/full_data', 'r') as casefile:
    grid = casefile.read().splitlines()
startTime = time.time()
count = 0



def test(y,x, map):
    if clamp(x,0,len(grid)-1 ) == x and clamp(y,0,len(grid[0])-1 ) == y:
        if grid[y][x] == "@":
            return 1
    return 0

i = 0
while i < 100:


    row = 0
    while row < len(grid[0]):
        col = 0
        while col < len(grid):
            if grid[row][col] == "@":
                neighbors = 0
                neighbors += test(row - 1, col - 1, grid)
                neighbors += test(row - 1, col, grid)
                neighbors += test(row - 1, col + 1, grid)

                neighbors += test(row, col - 1, grid)
                neighbors += test(row, col + 1, grid)

                neighbors += test(row + 1, col - 1, grid)
                neighbors += test(row + 1, col, grid)
                neighbors += test(row + 1, col + 1, grid)

                if neighbors < 4:
                    count += 1
                    grid[row] = grid[row][0:col] + '.' + grid[row][col+1:len(grid)]

            col += 1
        row += 1


    i += 1



print(green("count: " + str(count)))
timerstop(startTime)