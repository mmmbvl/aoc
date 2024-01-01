inp = open("input").readlines()

from heapq import heappop, heappush
# import functools
from typing import NamedTuple

min_straight_moves = 0
max_straight_moves = 3

directions = ["N", "W", "S", "E"]
directions_change = {
    0: [-1, 0],
    1: [ 0,-1],
    2: [ 1, 0],
    3: [ 0, 1]
}

CCWturn_lookup = {
    0: 1,
    1: 2,
    2: 3,
    3: 0
}

city = []
for line in inp:
    city.append(list(filter(lambda x : x != "\n", list(line))))

def turn_dirCCW(d: int):
    return (d + 4 + 1) % 4
def turn_dirCW(d: int):
    return (d + 4 - 1) % 4

# Coordinates = NamedTuple('Coordinates', [('r', int), ('c', int), ('dir', int)])
Employee = NamedTuple('Employee', [('name', str), ('id', int)])
class Coordinates(NamedTuple):

#     # __slots__ = ()
#     # _fields = ('r', 'c', 'dir')

    r: int
    c: int
    dir: int

    # def __init__(self, row, col, dir):
    #     self.r = row
    #     self.c = col
    #     self.dir = dir
    # @property
    # def move_fwd(self) -> "Coordinates":
    #     return Coordinates(self.r + directions_change[self.dir][0], self.c + directions_change[self.dir][1], dir)

    # def turn_CCW(self) -> "Coordinates":
    #     return Coordinates(self.r, self.c, turn_dirCCW(self.dir))

    # def turn_CW(self) -> "Coordinates":
    #     return Coordinates(self.r, self.c, turn_dirCW(self.dir))
    
    # def __eq__(self, other):
    #     return self.r == other.r and self.c == other.c and self.dir == other.dir
    
    # def __lt__(self, other):
    #     if self.r < other.r:
    #         return True
    #     elif self.r == other.r:
    #         if self.c < other.c:
    #             return True
    #         elif self.c == other.c:
    #             if self.dir == other.dir:
    #                 return True
    #     return False

def turn_CCW(self) -> "Coordinates":
    return Coordinates(self.r, self.c, (self.dir + 4 + 1) % 4)

def move_fwd(self) -> "Coordinates":
    return Coordinates(self.r + directions_change[self.dir][0], self.c + directions_change[self.dir][1], self.dir)


def turn_CW(self) -> "Coordinates":
    return Coordinates(self.r, self.c, (self.dir + 4 - 1) % 4)


endpoint = Coordinates(len(city) - 1, len(city[0]) - 1, 0)

State = tuple[int, Coordinates, int]
def solve(part):
    if part == "P1":
        queue: list[State] = [
            (0, Coordinates(0, 0, 2), 0),
            (0, Coordinates(0, 0, 3), 0)
        ]
        seen: set[tuple[Coordinates, int]] = set()

        while queue:
            cost, pos, num_steps = heappop(queue)
            # print(pos)
            if pos.r == endpoint.r and pos.c == endpoint.c and num_steps >= min_straight_moves:
                return cost

            if (pos, num_steps) in seen:
                continue
            seen.add((pos, num_steps))

            # (fwd_pt) = pos.move_fwd()
            # (left_pt := pos.turn_CCW().move_fwd())
            # (right_pt := pos.turn_CW().move_fwd())

            left_pt = move_fwd(turn_CCW(pos))
            right_pt = move_fwd(turn_CW(pos))
            fwd_pt = move_fwd(pos)

            if (num_steps >= min_straight_moves and left_pt.r >= 0 and left_pt.r < len(city) and left_pt.c >= 0 and left_pt.c < len(city[0])):
                heappush(queue, (cost + int(city[left_pt.r][left_pt.c]), left_pt, 1))

            if (num_steps >= min_straight_moves and right_pt.r >= 0 and right_pt.r < len(city) and right_pt.c >= 0 and right_pt.c < len(city[0])):
                heappush(queue, (cost + int(city[right_pt.r][right_pt.c]), right_pt, 1))

            if (num_steps < max_straight_moves and fwd_pt.r >= 0 and fwd_pt.r < len(city) and fwd_pt.c >= 0 and fwd_pt.c < len(city[0])):
                heappush(queue, (cost + int(city[fwd_pt.r][fwd_pt.c]), fwd_pt, num_steps + 1))

        return -1

print("P1: ", solve("P1"))