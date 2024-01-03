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

num_in_trench = 0
for inst in instructions:
    move_ch = directions[inst[0]]
    display(inst, curr_pos, grid)
    for i in range(inst[1]):
        grid[curr_pos[0]][curr_pos[1]] = "#"
        num_in_trench += 1
        curr_pos[0] += move_ch[0]
        curr_pos[1] += move_ch[1]

inside_pt = [750,750]
outside_pt = [0,0]
num_digged = 0
# for r in range(len(grid)):
#     is_inside = False
#     for c in range(len(grid[0])):
#         if r % 50 == 0 and r > 600:
#             if c % 100 == 0:
#                 display(instructions[-1], [r,c], grid)
#                 time.sleep(1)
#         if grid[r][c] == "#" and is_inside == False:
#             is_inside = True
#             num_digged += 1
#         elif grid[r][c] == "#" and is_inside == True:
#             num_digged += 1
#             is_inside = False
#         elif is_inside == True:
#             grid[r][c] = "#"
#             num_digged += 1
#         else:
#             continue

def flood(pt, ch):
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

# flood(outside_pt, "G")
flood(inside_pt, "A")
ng = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "G": ng += 1
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "A": num_in_trench += 1


print("P1: ", (len(grid) * len(grid[0])) - ng)
print("P1: ", num_in_trench)




new_instructions = []
for n in instructions:
    k = n[2][2:-1]
    dir_h = k[-1]
    if dir_h == "0":
        dir_h = "R"
    if dir_h == "1":
        dir_h = "D"
    if dir_h == "2":
        dir_h = "L"
    if dir_h == "3":
        dir_h = "U"
    amt = int(k[:-1],16)
    new_instructions.append((dir_h,amt,""))
# 111329 too high
    



size = [0, 0, 0, 0]
for inst in new_instructions:
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
    print("coreezon", r, size[0] + size[2])
    grid.append([])
    for c in range(size[1] + size[3]):
        grid[-1].append(".")

curr_pos = [size[0], size[1]]
print("G","G")
num_in_trench = 0
for inst in new_instructions:
    move_ch = directions[inst[0]]
    display(inst, curr_pos, grid)
    for i in range(inst[1]):
        grid[curr_pos[0]][curr_pos[1]] = "#"
        num_in_trench += 1
        curr_pos[0] += move_ch[0]
        curr_pos[1] += move_ch[1]


inside_pt = [size[0] - 20,size[1] - 20]

flood(inside_pt, "A")
ng = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "G": ng += 1
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "A": num_in_trench += 1


# print("P1: ", (len(grid) * len(grid[0])) - ng)
print("P2: ", num_in_trench)
