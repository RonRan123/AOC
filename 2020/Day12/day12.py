import math
data = [(line[0], int(line[1:])) for line in open("input12.txt", "r").readlines()]
# Part 1
x, y = 0, 0
rotation = 90
for d in data:
    # print(x, y, rotation, d)
    direction, amt = d
    if direction == "R":
        rotation += amt
    elif direction == "L":
        rotation -= amt
    elif direction == "N":
        y += amt
    elif direction == "S":
        y -= amt
    elif direction == "E":
        x += amt
    elif direction == "W":
        x -= amt
    elif direction == "F":
        rotation = rotation % 360
        tmp = rotation/90
        if tmp >=2:
            amt = amt*-1
        if tmp%2 ==0:
            y += amt
        else:
            x += amt
x, y = abs(x), abs(y)
print(x, y, x+y)


# Part 2
x, y = 0, 0
wx, wy = 10, 1
rotation = 0
for d in data:
    print(x, y, wx, wy, d)
    direction, amt = d
    if direction == "R" or direction == "L":
        rad = amt/180 * math.pi
        if direction == "R":
            rad = rad * -1
        newx = wx*math.cos(rad) - wy*math.sin(rad)
        newy = wy*math.cos(rad) + wx*math.sin(rad)
        wx, wy = newx, newy
        rotation += amt
    elif direction == "N":
        wy += amt
    elif direction == "S":
        wy -= amt
    elif direction == "E":
        wx += amt
    elif direction == "W":
        wx -= amt
    elif direction == "F":
        x += amt*wx
        y += amt*wy
x, y = abs(x), abs(y)
print(x, y, x+y)