inp = open("input").readlines()

import time
import os

lava_map = []
for line in inp:
    lava_map.append(list(filter(lambda x : x != "\n", list(line))))

energized_map = [list(map(lambda x: 0, row)) for row in lava_map]

directions_changing = {
    "\\":   {"N": "W", "E": "S", "S": "E", "W": "N"},
    "/":    {"N": "E", "W": "S", "S": "W", "E": "N"}
}
directions_m = {
    "N": [-1, 0],
    "S": [ 1, 0],
    "E": [ 0, 1],
    "W": [ 0,-1]
}

def display():
    os.system('clear')
    print("Showing the map with laser pathing:")
    for r in range(len(lava_map) - 55):
        disp = lava_map[r][:55]
        for c in range(len(disp)):
            if lava_map[r][c] == "." and energized_map[r][c] != 0:
                disp[c] = str(energized_map[r][c])
        print("  ".join(disp))

class Laser():
    def __init__(self, row, col, dir):
        self.row = row
        self.col = col
        self.dir = dir
    def move(self):
        self.row += directions_m[self.dir][0]
        self.col += directions_m[self.dir][1]
    def change_direction(self, new_dir):
        self.dir = new_dir
    def show(self):
        return "$Laser [R:" + str(self.row) + "  C:" + str(self.col) + "] D:" + self.dir + "$"

def propagate_lasers(start_laser, lava_map):
    lasers = []
    lasers.append(start_laser)
    previous_lasers = [start_laser.show()]

    while len(lasers) != 0:
        # time.sleep(0.6)
        # print("\n\nLasers:")
        # for l in lasers:
        #     print(l.show())
        lasers[0].move()
        display()
        print(lasers[0].row, lasers[0].col, lasers[0].dir)
        # print(previous_lasers, lasers[0].show())
 
        if not lasers[0].show() in previous_lasers:
            previous_lasers.append(lasers[0].show())
        else:
            # print("Removed duplicate laser: ", lasers[0].show())
            lasers.pop(0)
            continue

        if lasers[0].row < 0 or lasers[0].row >= len(lava_map) or lasers[0].col < 0 or lasers[0].col >= len(lava_map[0]):
            print("Removed a laser")
            lasers.pop(0)
            continue

        interacting_square = lava_map[lasers[0].row][lasers[0].col]
        energized_map[lasers[0].row][lasers[0].col] += 1

        if interacting_square == ".":
            "do nothing"
        elif interacting_square == "\\" or interacting_square == "/":
            lasers[0].change_direction(directions_changing[interacting_square][lasers[0].dir])
        elif interacting_square == "-":
            if lasers[0].dir == "N" or lasers[0].dir == "S":
                lasers[0].change_direction("E")
                lasers.append(Laser(lasers[0].row, lasers[0].col, "W"))
                print("Added a laser vert", interacting_square)
        else: # interacting_square == "|":
            if lasers[0].dir == "E" or lasers[0].dir == "W":
                print("To ad...", interacting_square, lasers[0].row, lasers[0].col, lasers[0].dir)
                lasers[0].change_direction("N")
                lasers.append(Laser(lasers[0].row, lasers[0].col, "S"))
                print("Added a laser horiz", interacting_square, lasers[0].row, lasers[0].col, lasers[0].dir)
                print(len(lasers))

def solve(part):

    if part == "P1":
        total = 0
        propagate_lasers(Laser(0,-1,"E"), lava_map)
        for r in energized_map:
            for c in r:
                if c != 0: total += 1
        print("P1: ", total)

solve("P1")
                