# part 1
import numpy as np

with open("day12.txt") as df:
    instructions = df.read().splitlines()

# set initial coordinates and direction
x = 0
y = 0
dir = 0 # 0 is east, 1 is north, 2 is west, 3 is south

def move(line):
    global x,y,dir

    if line[0] == "N":
        y += int(line[1:])
    elif line[0] == "S":
        y += - int(line[1:])
    elif line[0] == "W":
        x += - int(line[1:])
    elif line[0] == "E":
        x += int(line[1:])
    elif line[0] == "L":
        dir = (dir + int(int(line[1:])/90)) % 4
    elif line[0] == "R":
        dir = (dir - int(int(line[1:])/90)) % 4
    elif line[0] == "F":
        if dir == 0:
            move("E"+line[1:])
        elif dir == 1:
            move("N"+line[1:])
        elif dir == 2:
            move("W" + line[1:])
        elif dir == 3:
            move("S" + line[1:])

def Manhattan(x,y):
    return abs(x) + abs(y)

for line in instructions:
    move(line)

print(f"The final Manhattan distance is {Manhattan(x,y)}")

# part 2

def sin(angle):
    return {0:0, 90:1, 180:0, 270:-1}[angle % 360]

def cos(angle):
    return {0:1, 90:0, 180:-1, 270:0}[angle % 360]

# set initial coordinates
x = 0
y = 0
xway = 10
yway = 1

def move(line):
    global x,y,xway,yway

    if line[0] == "N":
        yway += int(line[1:])
    elif line[0] == "S":
        yway += - int(line[1:])
    elif line[0] == "W":
        xway += - int(line[1:])
    elif line[0] == "E":
        xway += int(line[1:])
    elif line[0] == "L":
        dx = (xway - x)
        dy = (yway - y)
        xway = int(dx * cos(int(line[1:])) - dy * sin(int(line[1:])) + x)
        yway = int(dx * sin(int(line[1:])) + dy * cos(int(line[1:])) + y)
    elif line[0] == "R":
        dx = (xway - x)
        dy = (yway - y)
        xway = int(dx * cos(- int(line[1:])) - dy * sin(- int(line[1:])) + x)
        yway = int(dx * sin(- int(line[1:])) + dy * cos(- int(line[1:])) + y)
    elif line[0] == "F":
        xdiff = int(line[1:]) * (xway - x)
        ydiff = int(line[1:]) * (yway - y)

        x += xdiff
        xway += xdiff # waypoint moves with the ship
        y += ydiff
        yway += ydiff

for line in instructions:
    move(line)

print(f"The final Manhattan distance is {Manhattan(x, y)}")