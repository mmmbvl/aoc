inp = open("input").readlines()

patterns = [[]]
for line in inp:
    if line == "\n":
        patterns.append([])
    else:
        patterns[-1].append(list(line.split("\n")[0])) 

def find_hori_LOR(p, part):
    mistakes = {}

    for p_lor in range(1,len(p)):
        bi = p_lor - 1
        ui = p_lor

        ms = 0
        while bi >= 0 and ui < len(p):
            for a in range(len(p[0])):
                if p[bi][a] != p[ui][a]:
                    ms += 1
            bi -= 1
            ui += 1
        mistakes[p_lor] = ms

    for i in mistakes:
        if mistakes[i] == 1 if part == "P2" else mistakes[i] == 0:
            return i
    return 0

def transp(mtx):
    new_mtx = []
    for c in range(len(mtx[0])):
        new_mtx.append([mtx[r][c] for r in range(len(mtx))])
    return new_mtx

def solve(patterns, part):
    tot = 0
    for p in patterns:
        tot += (100 * find_hori_LOR(p, part)) + find_hori_LOR(transp(p), part)
    print(part, ": ", tot)

solve(patterns, "P1")
solve(patterns, "P2")


