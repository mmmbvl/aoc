inp = open("input").readlines()

platform = [list(x.split("\n")[0]) for x in inp]

def roll_rocks(pf):
    for c in range(len(pf[0])):
        last_empty = 0
        for r in range(len(pf)):
            if pf[r][c] == "#":
                last_empty = r + 1
            
            if pf[r][c] == "O":
                if last_empty == r:
                    last_empty = r + 1
                else:
                    pf[last_empty][c] = "O"
                    pf[r][c] = "."

                    next_empty = last_empty
                    while next_empty < len(pf) - 1 and pf[next_empty][c] != ".":
                        next_empty += 1
                    last_empty = next_empty
    return pf

def rotate_platform(platform, dir):
    pf = []
    if dir == "N":
        for r in range(len(platform)):
            pf.append(platform[r][:]) 
    if dir == "W":
        for c in range(len(platform[0])):
            new_row = []
            for r in range(len(platform)):
                new_row.append(platform[(len(platform) - 1) -r][c])
            pf.append(new_row)
    return pf

def weigh(platform):
    tot = 0
    for r in range(len(platform)):
        for c in range(len(platform[0])):
            if platform[r][c] == "O": tot += len(platform) - r
    return tot

def cycle(platform):
    weighs = []

    for d in ["N", "W", "W", "W"]:
        platform = rotate_platform(platform, d)
        platform = roll_rocks(platform)
        weighs.append(weigh(platform))
        print(weigh(platform))
    platform = rotate_platform(platform, "W")
    return [platform, weighs]
# print("\n\nOriginal Platform")
# for p in platform:
#     print(p[0:25])

# print("\n\nRolled Platform")
# for p in roll_rocks(platform):
#     print(p[0:25])
    
def solve(platform, part):
    if part == "P1":
        print("P1: ", weigh(roll_rocks(platform)))
    if part == "P2":
        previous_weights = [0]
        cyc = 0

        for i in range(1000000000):
            nyr = cycle(platform)
            platform = nyr[0]
            previous_weights += nyr[1]
            # print(i, previous_weights[-1])

            is_steady_state = False
            for cycle_length in range(1, len(previous_weights)):
                is_cycle = True
                for j in range(len(previous_weights) - 1, len(previous_weights) - 1 - cycle_length,-1):
                    if previous_weights[j] != previous_weights[j - cycle_length]:
                        is_cycle = False
                        break

                if is_cycle and i > 1000:
                    print("Cycle found with length: ", cycle_length)
                    is_steady_state = True
                    cyc = cycle_length
                    break
            if is_steady_state:
                break
        
        weight_at_billion = 0
        for k in range(len(previous_weights) - 1, 0, -1):
            if (1000000000 - k) % cyc == 0:
                weight_at_billion = previous_weights[k]
                break
        print("P2: ", weight_at_billion)

solve(platform, "P1")
solve(platform, "P2")

# 142839 too high
# 106576 too high
