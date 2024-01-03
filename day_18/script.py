inp = open("input").readlines()

import os
import time

def process_instructions(inp):
    instructions = []
    for line in inp:
        p = "".join((filter(lambda x: x != "\n", list(line)))).split(" ")
        p[2] = p[2][1:-1]
        instructions.append((p[0], int(p[1]), p[2]))
    return instructions

directions = {
    "U": [-1, 0],
    "D": [ 1, 0],
    "L": [ 0,-1],
    "R": [ 0, 1]
}

def define_grid_size(instructions):
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
    return size

def make_grid(instructions, size):
    grid = []
    for r in range(size[0] + size[2]):
        grid.append([])
        for c in range(size[1] + size[3]):
            grid[-1].append(".")
    return grid

def display(mv, curr_pos, grid):
    limit_row = 50
    limit_col = 150

    a = int(curr_pos[0] - (limit_row/2)) if int(curr_pos[0] - (limit_row/2)) >= 0 else 0
    b = int(curr_pos[0] + (limit_row/2)) if int(curr_pos[0] + (limit_row/2)) < len(grid) else len(grid) - 1
    c = int(curr_pos[1] - (limit_col/2)) if int(curr_pos[0] - (limit_col/2)) >= 0 else 0
    d = c + limit_col if c + limit_col < len(grid[0]) else len(grid[0]) - 1
    # d = int(curr_pos[1] + (limit_col/2)) if int(curr_pos[0] + (limit_col/2)) < len(grid[0]) else len(grid[0]) - 1

    os.system("clear")
    print("Current grid")
    print("Move: ", mv)
    print(a, b, c, d)
    for row in grid[a:b]:
        print("".join(row[c:d]))
    time.sleep(0.01)

def carve_instructions(instructions, grid, size):
    curr_pos = [size[0], size[1]]
    for inst in instructions:
        move_ch = directions[inst[0]]
        display(inst, curr_pos, grid)
        for i in range(inst[1]):
            grid[curr_pos[0]][curr_pos[1]] = "#"
            curr_pos[0] += move_ch[0]
            curr_pos[1] += move_ch[1]
    return grid

def flood(grid, pt, ch, instructions):
    arr = []
    arr.append(pt)

    while arr:
        px = arr.pop(0)
        grid[px[0]][px[1]] = ch
        print(px)

        if px[0] % 25 == 0 and px[0] > 500:
            if px[1] % 25 == 0 and px[1] > 500:
                display(instructions[-1], px, grid)

        for d in directions:
            new_pt = [px[0] + directions[d][0], px[1] + directions[d][1]]
            if new_pt[0] >= 0 and new_pt[1] >= 0 and new_pt[0] < len(grid) and new_pt[1] < len(grid[0]) and grid[new_pt[0]][new_pt[1]] == ".":
                grid[new_pt[0]][new_pt[1]] = ch
                arr.append(new_pt)
    return grid

def count_dug(grid):
    num_dug = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#": num_dug += 1
    return num_dug

def solve(part):
    if part == "P1":
        inst = process_instructions(inp)
        sz = define_grid_size(inst)
        grd = make_grid(inst, sz)
        grd = carve_instructions(inst, grd, sz)
        grd = flood(grd, [sz[0] - 20, sz[1] - 20], "#", inst)
        num_dug = count_dug(grd)
        print("P1: ", num_dug)

solve("P1")