inp = open("input").readlines()

import time
import os
from heapq import heappop, heappush
import functools

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
        # new_d += [1, 3]
        new_d += [3]
    if d == 1 or d == 3:
        # new_d += [0, 2]
        new_d += [2]
    return new_d

class Node():
    def __init__(self, r, c, dir, moves_remaining):
        self.r = r
        self.c = c
        self.dir = dir
        self.next_moves = []
        self.moves_remaining = moves_remaining
        self.weight = int(city[r][c])
        self.cost = 10000000
        # if self.dir == "N" or self.dir == "W":
        #     self.weight += 12
        self.seen = False
    
    def add_connected(self, cd):
        self.next_moves.append(cd)

    def update_lowest_cost(self, cost):
        # print("Trying to update cost: existing:", self.cost, "\tweight:", self.weight, "\tnew:", cost + self.weight)

        if self.cost == -1:
            self.cost = cost + self.weight
        elif cost + self.weight < self.cost:
            self.cost = cost + self.weight
        else:
            # print("Higher cost -- do not update")
            return "higher cost than previously found"
        # print("Has been updated:\t\t",self.cost)
        return "updated, lower cost than previously found"
    
    def display(self):
        disp = "Noder\nR:"+str(self.r)+ "\t\tC:"+ str(self.c)+ "\tD:"+ self.dir + "\n" + "moves_rem: " + str(self.moves_remaining) + "\tW:" + str(self.weight) + "\tCost:" + str(self.cost)
        disp += "\nConnected Nodes: " + "".join(["===" + str(n.r) + "," + str(n.c) + "," + n.dir + "," + str(n.moves_remaining) for n in self.next_moves])
        return disp
    
    def __eq__(self, other):
        return self.cost == other.cost
    
    def __lt__(self, other):
        return self.cost < other.cost


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
                    if new_r >= 0 and new_c >= 0 and new_r < len(city) and new_c < len(city[0]):
                        # print("adding connected: ", r, c, "====>", new_r, new_c)
                        graph[r][c][d][moves_remaining].add_connected(graph[new_r][new_c][new_d][max_straight_moves - 1])
                if moves_remaining > 0:
                    new_r = r + directions_change[d][0]
                    new_c = c + directions_change[d][1]
                    if new_r >= 0 and new_c >= 0 and new_r < len(city) and new_c < len(city[0]):
                        graph[r][c][d][moves_remaining].add_connected(graph[new_r][new_c][d][moves_remaining - 1])

# starting graph nodes
start_E = Node(0, 0, "E", 3)
start_E.add_connected(graph[1][0][2][2])
start_E.add_connected(graph[0][1][3][2])

est_total_num_nodes = len(city) * len(city[0]) * 4 * 3

dbg_row_limit = 45
dbg_col_limit = 100

# traversa;
def find_path():
    nodes_processed = 0

    nodes_to_examine = []
    nodes_to_examine.append(start_E)

    path_costs = []
    path_costs.append(0)

    while len(nodes_to_examine) != 0:
        # curr_node = nodes_to_examine.pop(0)
        # assoc_weight = path_costs.pop(0)
        curr_node = heappop(nodes_to_examine)
        assoc_weight = heappop(path_costs)

        try_update = curr_node.update_lowest_cost(assoc_weight)


        nodes_processed += 1
        # time.sleep(0.13)
        os.system("clear")
        print("Processed ", nodes_processed, " of expected ", est_total_num_nodes, " nodes")

        print("-------------------------------------------------\nCurrent Node:")
        print(curr_node.display())


        curr_node.seen = True
        if try_update == "updated, lower cost than previously found":
            # print("\nAdd These Nodes:")
            for nd in curr_node.next_moves:

                # is_seen = False
                # for d in range(len(directions)):
                #     for moves_remaining in range(max_straight_moves):
                #         stack_node = graph[nd.r][nd.c][d][moves_remaining]
                #         if stack_node.seen:
                #             is_seen = True
                is_seen = False
                if not is_seen:
                        # nodes_to_examine.append(nd)
                        # path_costs.append(curr_node.cost)
                        heappush(nodes_to_examine,nd)
                        heappush(path_costs,curr_node.cost)




                # min_current_cost_stack = 10000000000
                # for d in range(len(directions)):
                #     for moves_remaining in range(max_straight_moves):
                #         stack_node = graph[nd.r][nd.c][d][moves_remaining]
                #         if stack_node.cost != -1 and stack_node.cost < min_current_cost_stack:
                #             min_current_cost_stack = stack_node.cost

                # if min_current_cost_stack > curr_node.cost + nd.weight:
                #     if (nd.dir == "S" or nd.dir == "E"):
                #         nodes_to_examine.insert(0,nd)
                #         path_costs.insert(0,curr_node.cost)
                #     else:
                #         nodes_to_examine.append(nd)
                #         path_costs.append(curr_node.cost)
                    # print(nd.display())

        print("\nExamining current map:")
        for rdbg in range(len(city))[0:dbg_row_limit]:
            dbg_string = "".join(city[rdbg][0:dbg_col_limit])
            if rdbg == curr_node.r:
                dbg_string = "".join(dbg_string[:curr_node.c] + "@" + dbg_string[curr_node.c + 1:])
            print(dbg_string)

def solve(part):
    if part == "P1":
        find_path()
        min_cost = 1000000
        for d in range(len(directions)):
            for moves_remaining in range(max_straight_moves):
                test = graph[len(city) - 1][len(city[0]) - 1][d][moves_remaining].cost
                if test < min_cost:
                    min_cost = test

        print("P1: ", min_cost)

solve("P1")

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