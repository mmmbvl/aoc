inp = open("input").readlines()

max_straight_moves = 3
directions = ["N", "W", "S", "E"]
directions_change = {
    0: [-1, 0],
    1: [ 0,-1],
    2: [ 1, 0],
    3: [ 0, 1]
}

city = []
for line in inp:
    city.append(list(filter(lambda x : x != "\n", list(line))))

def turn_dir(d):
    new_d = []
    # if d == "N" or d == "S":
    #     new_d += ["E", "W"]
    # if d == "W" or d == "E":
    #     new_d += ["N", "S"]
    if d == 0 or d == 2:
        new_d += [1, 2]
    if d == 1 or d == 3:
        new_d += [0, 2]
    return new_d

class Node():
    def __init__(self, r, c, dir, moves_remaining):
        self.r = r
        self.c = c
        self.dir = dir
        self.next_moves = []
        self.moves_remaining = moves_remaining
        self.weight = city[r][c]
    
    def add_connected(self, cd):
        self.next_moves.append(cd)

# generate all possible nodes
graph = []
for r in range(len(city)):
    graph.append([])
    for c in range(len(city[0])):
        graph[-1].append([])
        for d in range(len(directions)):
            dir = directions[d]
            graph[-1][-1].append([])
            for moves_remaining in range(max_straight_moves):
                graph[r][c][d].append(Node(r,c,dir,moves_remaining))

# connect graph nodes
for r in range(len(city)):
    for c in range(len(city[0])):
        for d in range(len(directions)):
            for moves_remaining in range(max_straight_moves):
                for new_d in turn_dir(d):
                    new_r = r + directions_change[new_d][0]
                    new_c = c + directions_change[new_d][1]
                    if new_r > 0 and new_c > 0 and new_r < range(len(city)) and new_c < range(len(city[0])):
                        graph[r][c][d][moves_remaining].connect(graph[new_r][new_c][new_d][max_straight_moves - 1])
                if moves_remaining > 0:
                    new_r = r + directions_change[d][0]
                    new_c = c + directions_change[d][1]
                    if new_r > 0 and new_c > 0 and new_r < range(len(city)) and new_c < range(len(city[0])):
                        graph[r][c][d][moves_remaining].connect(graph[new_r][new_c][d][moves_remaining - 1])

# starting graph nodes
start_E = Node(0, 0, "E", 3)
start_E.connect(graph[1][0][2][2])
start_E.connect(graph[0][1][3][2])



# row, column, direction, moves left
# cannot travel backwards
# in direction of travel, has limited moves left: 2, 1, or 0
# turning, has full moves left: 3, 2, 1, 0
# when gets to 0 moves left, no longer connected in direction of travel
# [r, c, dir="E", moves=2] ==>  [r, c+1, dir="E", moves=> moves-1 = 1]
#                               [r-1, c, dir="N", moves=> MAX_MOVES-1 =2]
#                               [r+1, c, dir="S", moves=> MAX_MOVES-1 =2]
# [r, c, dir="E", moves=1] ==>  [r, c+1, dir="E", moves=> moves-1 = 0]
#                               [r-1, c, dir="N", moves=> MAX_MOVES-1 =2]
#                               [r+1, c, dir="S", moves=> MAX_MOVES-1 =2]
# [r, c, dir="E", moves=0] ==>  X - no longer available - [r, c+1, dir="E", moves=> moves-1 = 0]
#                               [r-1, c, dir="N", moves=> MAX_MOVES-1 =2]
#                               [r+1, c, dir="S", moves=> MAX_MOVES-1 =2]