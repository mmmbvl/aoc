inp = open("input").readlines()

import os
import time

instructions = []
for line in inp:
    p = "".join((filter(lambda x: x != "\n", list(line)))).split(" ")
    p[2] = p[2][1:-1]
    instructions.append((p[0], int(p[1]), p[2]))

directions = {
    "U": [-1, 0],
    "D": [ 1, 0],
    "L": [ 0,-1],
    "R": [ 0, 1]
}

size = [0, 0, 0, 0]
for inst in instructions:
    if inst[0] == "U":
        size[0] += inst[1]
    if inst[0] == "D":
        size[2] += inst[1]
    if inst[0] == "L":
        size[1] += inst[1]
    if inst[0] == "R":
        size[3] += inst[1]

print(size)

grid = []
for r in range(size[0] + size[2]):
    grid.append([])
    for c in range(size[1] + size[3]):
        grid[-1].append(".")

curr_pos = [size[0], size[1]]

def display(mv, curr_pos):
    limit_row = 50
    limit_col = 150

    a = int(curr_pos[0] - (limit_row/2))
    b = int(curr_pos[0] + (limit_row/2))
    c = int(curr_pos[1] - (limit_col/2))
    d = int(curr_pos[1] + (limit_col/2))

    os.system("clear")
    print("Current grid")
    print("Move: ", mv)
    for row in grid[a:b]:
        print("".join(row[c:d]))
    time.sleep(0.05)

for inst in instructions:
    move_ch = directions[inst[0]]
    display(inst, curr_pos)
    for i in range(inst[1]):
        grid[curr_pos[0]][curr_pos[1]] = "#"
        curr_pos[0] += move_ch[0]
        curr_pos[1] += move_ch[1]