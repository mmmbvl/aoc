inp = open("input").readlines()

platform = [list(x.split("\n")[0]) for x in inp]

def roll_rocks(platform):
    # platform = platform[:]
    pf = []
    for p in platform:
        pf.append(p[:])
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

def weigh(platform):
    tot = 0
    for r in range(len(platform)):
        for c in range(len(platform[0])):
            if platform[r][c] == "O": tot += len(platform) - r
    return tot

# print("\n\nOriginal Platform")
# for p in platform:
#     print(p[0:25])

# print("\n\nRolled Platform")
# for p in roll_rocks(platform):
#     print(p[0:25])
    
def solve(platform, part):
    if part == "P1":
        print("P1: ", weigh(roll_rocks(platform)))

solve(platform, "P1")