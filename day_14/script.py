inp = open("input").readlines()

platform = [list(x.split("\n")[0]) for x in inp]

def rotate_platform_90(platform):
    pf = []
    for c in range(len(platform[0])):
        new_row = []
        for r in range(len(platform)):
            new_row.append(platform[(len(platform) - 1) -r][c])
        pf.append(new_row)
    return pf

def roll_rocks(pf, dir):
    pf = pf[:]
    d = {
         "N": 0,
         "W": 1,
         "S": 2,
         "E": 3
         }
    for i in range(d[dir]):
        pf = rotate_platform_90(pf)
    
    
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

    for i in range(4 - d[dir]):
        pf = rotate_platform_90(pf)    

    return pf

def weigh(platform):
    tot = 0
    for r in range(len(platform)):
        for c in range(len(platform[0])):
            if platform[r][c] == "O": tot += len(platform) - r
    return tot
    
def solve(platform, part):
    if part == "P1":
        print("P1: ", weigh(roll_rocks(platform, "N")))
    if part == "P2":
        previous_weights = [0]
        cyc = 0

        for i in range(1000000000):
            dir = ["N", "W", "S", "E"][i % 4]
            platform = roll_rocks(platform, dir)
            if i % 4 == 2: previous_weights.append(weigh(platform))
            print(i, previous_weights[-1])

            is_steady_state = False
            for cycle_length in range(4, len(previous_weights)):
                is_cycle = True
                for j in range(len(previous_weights) - 1, len(previous_weights) - 1 - cycle_length,-1):
                    if previous_weights[j] != previous_weights[j - cycle_length]:
                        is_cycle = False
                        break

                if is_cycle and i > 3000:
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

# 2961 98812
# 2962 90785
# 2963 90785
# 2964 98821
# 2965 98821
# 2966 90787
# 2967 90787
# 2968 98809
# 2969 98809
# 2970 90781
# 2971 90781
# 2972 98822
# 2973 98822
# 2974 90790
# 2975 90790
# 2976 98807
# 2977 98807
# 2978 90784
# 2979 90784
# 2980 98819
# 2981 98819
# 2982 90796
# 2983 90796
# 2984 98818
# 2985 98818
# 2986 90794
# 2987 90794
# 2988 98827
# 2989 98827
# 2990 90795
# 2991 90795
# 2992 98809
# 2993 98809
# 2994 90788
# 2995 90788
# 2996 98823
# 2997 98823
# 2998 90792
# 2999 90792
# 3000 98810
# 3001 98810
