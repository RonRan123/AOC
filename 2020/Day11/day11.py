import copy
import numpy as np

def checkArea(row, col):
    global data
    tmp = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if 0 <= x+row < len(data) and 0 <= y+col < len(data[0]):
                tmp.append((x+row, y+col))
    tmp.remove((row, col))
    # print(sum([data[r][c]=="#" for r, c in tmp]))
    return sum([data[r][c]=="#" for r, c in tmp])


def checkFirst(row, col):
    global data
    if round == 1 and row == 7 and col == 9:
        print("reached")

    R, C = len(data), len(data[0])
    tmp = 0
    # # Occupied seat to the right
    # if "#" in data[row][col+1:]:
    #     tmp += 1
    # # Occupied seat to the left
    # if "#" in data[row][:col]:
    #     tmp += 1

    # vertical = [data[row][c] for c in range(len(data[0]))]
    # # Occupied seat down
    # if "#" in vertical[row+1:]:
    #     tmp += 1
    # # Occupied seat up
    # if "#" in vertical[:row]:
    #     tmp += 1

    # Copied from u/Chitinid when I couldn't think of a "creative" solution like above
    for x, y in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1,-1),(1, 0), (1, 1)]:
        r, c = row + x, col + y
        while (valid := (0 <= r < R and 0 <= c < C)) and data[r][c] == ".":
            r, c = r + x, c + y
        if valid and data[r][c] == "#":
            tmp += 1

    return tmp


def printGrid():
    global data
    for r in data:
        print("".join(r))
    print()


data = [list(line.strip()) for line in open("input11.txt", "r").readlines()]
print(len(data))
print(data[0])
change = 1
round = 0
while change != 0:
    print(round)
    printGrid()
    layout = copy.deepcopy(data)
    change = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            # print(data[r][c])
            if data[r][c] == "L":
                if checkFirst(r,c) == 0:
                    layout[r][c] = "#"
                    change += 1
            elif data[r][c] == "#":
                if checkFirst(r,c) >= 5:
                    layout[r][c] = "L"
                    change += 1

    data = layout
    round += 1

count = 0
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "#":
            count += 1
print(count)

