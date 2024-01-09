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

opposite_directions = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L"
}

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

def make_new_instructions(inst):
    # inst (dir, length, #color)
    new_inst = []
    curr_pos = [0, 0]
    new_inst.append(["U", 0, 0, 0])
    for x in inst:
        color = x[2][1:]
        new_dir = color[-1]
        if (new_dir == "0"):
            new_dir = "R"
        if (new_dir == "1"):
            new_dir = "D"
        if (new_dir == "2"):
            new_dir = "L"
        if (new_dir == "3"):
            new_dir = "U"
        new_length = int(color[:-1],16)

        move_ch = directions[x[0]]
        curr_pos[0] += move_ch[0] * new_length
        curr_pos[1] += move_ch[1] * new_length
        print("Turning old inst: ", x, " into new instruction: ", (new_dir, new_length, curr_pos[0], curr_pos[1]))
        new_inst.append((new_dir, new_length, curr_pos[0], curr_pos[1]))
    return new_inst

def reduce_collinear_inst(in1, in2):
    new_dir = "X"
    new_len = "X"

    dir1 = in1[0]
    dir2 = in2[0]

    rtn = ""

    if dir1 == dir2:
        new_dir = dir1
        new_len = in1[1] + in2[1]
        rtn = ("success", (new_dir, new_len, in2[2], in2[3]))
    elif dir2 == opposite_directions[dir1]:
        if in1[1] > in2[1]:
            new_dir = dir1
            new_len = in1[1] - in2[1]
            rtn = ("success", (new_dir, new_len, in2[2], in2[3]))
        if in2[1] > in1[1]:
            new_dir = dir2
            new_len = in2[1] - in1[1]
            return ("success", (new_dir, new_len, in2[2], in2[3]))
        else:
            rtn = ("cancelled out", "")
    else:
        rtn =("not collinear", "")

    print("Processing collinear ", in1, in2, " ===> ", rtn)
    return rtn

def reduce_boxlike_inst(in1, in2, in3):
    # CW : positive; CCW: negative
    rtn = ""
    if in3[0] == opposite_directions[in1[0]] and in2[0] != in1[0] and in2[0] != in3[0]:
        if in1[0] == "U" or in1[0] == "D":
            cwdir = 1
            if in1[0] == "D":
                cwdir *= -1
            if in2[0] == "L":
                cwdir *= -1
            midpoint = [in1[2],in2[3]]
            if midpoint[1] == in3[3]:
                rtn = ("success-c", cwdir * in2[1] * in1[1], (in2[0], in2[1], in3[2], in3[3]))
            else:
                new_dir = ""
                new_len = 0
                if in1[1] > in3[1]:
                    new_dir = in1[0]
                    new_len = in1[1] - in3[1]
                if in3[1] > in1[1]:
                    new_dir = in3[0]
                    new_len = in3[1] - in1[1]
                rtn =  ("success", cwdir * in2[1] * in1[1], (in2[0], in2[1], midpoint[0], midpoint[1]), (new_dir, new_len, in3[2], in3[3]))
        if in1[0] == "R" or in1[0] == "L":
            cwdir = 1
            if in1[0] == "U":
                cwdir *= -1
            if in2[0] == "L":
                cwdir *= -1
            midpoint = [in2[2],in1[3]]
            if midpoint[0] == in3[2]:
                rtn =  ("success-c", cwdir * in2[1] * in1[1], (in2[0], in2[1], in3[2], in3[3]))
            else:
                new_dir = ""
                new_len = 0
                if in1[1] > in3[1]:
                    new_dir = in1[0]
                    new_len = in1[1] - in3[1]
                if in3[1] > in1[1]:
                    new_dir = in3[0]
                    new_len = in3[1] - in1[1]
                rtn =  ("success", cwdir * in2[1] * in1[1], (in2[0], in2[1], midpoint[0], midpoint[1]), (new_dir, new_len, in3[2], in3[3]))
    else:
        rtn =  ("not boxlike", 0, "")
    
    print("Processing boxlike: ", in1, in2, in3, " ====> ", rtn)
    return rtn
    
def reduce_instructions(instructions):
    area = 0
    while instructions:
        os.system("clear")
        print("Current instruction length: ", len(instructions))
        time.sleep(0.1)
        if len(instructions) <= 2:
            break
        for i in range(1, len(instructions)):
            p = reduce_collinear_inst(instructions[i - 1], instructions[i])
            if p[0] == "success":
                instructions = instructions[:i-1] + [p[1]] + instructions[i+1:]
                break
            if p[0] == "cancelled out":
                instructions = instructions[:i-1] + instructions[i+1:]
                break
        print("No collinears")
        # time.sleep(0.12)
        for i in range(2, len(instructions)):
            p = reduce_boxlike_inst(instructions[i - 2], instructions[i-1], instructions[i])
            if p[0] == "success":
                instructions = instructions[:i-2] + [p[2]] + [p[3]] + instructions[i+1:]
                area += p[1]
                break
            if p[0] == "success-c":
                instructions = instructions[:i-2] + [p[2]] + instructions[i+1:]
                area += p[1]
                break
        print("No boxlikes")

        instructions = instructions[1:] + [instructions[0]]
        # time.sleep(0.12)
    return area

def shoelace_formula(instructions):
    area = 0
    for i in range(len(instructions)):
        y = instructions[i][3]
        xprev = instructions[((i - 1) + len(instructions)) % len(instructions)][2]
        xnext = instructions[((i + 1) + len(instructions)) % len(instructions)][2]
        area += y * (xprev + xnext)
    return area / 2


def greens_formula(instructions):
    x = 0
    y = 0
    area = 0
    perimeter = 0
    for i in range(len(instructions)):
        move_ch = directions[instructions[i][0]] 
        delta = [move_ch[0] * instructions[i][1], move_ch[1] * instructions[i][1]]
        x, y = x + delta[0], y + delta[1]
        area += y * delta[0]
        perimeter += instructions[i][1]
    return area + perimeter//2 + 1






def solve(part):
    if part == "P1":
        inst = process_instructions(inp)
        sz = define_grid_size(inst)
        grd = make_grid(inst, sz)
        grd = carve_instructions(inst, grd, sz)
        grd = flood(grd, [sz[0] - 20, sz[1] - 20], "#", inst)
        num_dug = count_dug(grd)
        print("P1: ", num_dug)
    if  part == "P2":
        inst = process_instructions(inp)
        new_inst = make_new_instructions(inst)
        answer = greens_formula(new_inst)
        # answer = shoelace_formula(new_inst)
        # answer = reduce_instructions(new_inst)
        print("P2: ", f'{answer:.20f}')

# solve("P1")
solve("P2")

# P2: 30170576447424 too low
# P2: 42708339569950
