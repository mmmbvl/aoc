inp = open("input").readlines()

patterns = [[]]
for line in inp:
    if line == "\n":
        patterns.append([])
    else:
        patterns[-1].append(list(line.split("\n")[0])) 

def print_patterns(ps, num):
    for i, m in enumerate(ps):
        if i == num - 1:
            print("\n\nPattern ", i+1)
            for j, n in enumerate(m):
                print(n)

# print_patterns(patterns)

def find_vert_LOR(p, dbg):
    t = []
    if dbg:
        print("Examining vertical lines of reflection")
    for r in p:
        if dbg:
            print("\n", r)
            dbgArr = ["_" for i in range(len(r) - 1)]
        for bp in range(1, len(r)):
            if dbg:
                dbgArr = ["_" for i in range(len(r) - 1)]
            if dbg:
                print(r[0:bp], list((r[bp:])))
            # isReflective = p[0:bp] == list(reversed(p[bp:]))
            isReflective = True
            for h in range(bp):
                if (bp - h) + bp - 1< len(r) and r[h] != r[(bp - h) + bp - 1]:
                    if dbg:
                        print("hit falsity: ", h, r[h], r[(bp - h + bp) - 1])
                    isReflective = False
            if dbg:
                print(isReflective, bp)

            if (isReflective):
                if not bp in t:
                    t.append(bp)
            else:
                if bp in t:
                    t.remove(bp)
            if dbg:
                dbgArr.insert(bp,"^")
            if dbg:
                print(dbgArr)
    return t

def find_hori_LOR(p, dbg):
    lor = 0
    xt = []
    possible_lors = range(1,len(p))

    for p_lor in possible_lors:
        bi = p_lor - 1
        ui = p_lor
        isReflective = True
        while bi >= 0 and ui < len(p):

            if "".join(p[bi]) != "".join(p[ui]):
                isReflective = False
            bi -= 1
            ui += 1
        if dbg:
            print("\n\n")
            for qw in range(len(p)):
                if qw == p_lor: print("--------------------------", isReflective, p_lor)
                print(p[qw])        
        if isReflective: lor = p_lor
        if isReflective: xt.append(p_lor)
    return lor

def transp(mtx):
    new_mtx = []
    # print("\n\nTranspose: ")

    for c in range(len(mtx[0])):
        new_mtx.append([])
        for r in range(len(mtx)):
            new_mtx[len(new_mtx) - 1].append(mtx[r][c])

    # for q in mtx:
    #     print(q)
    # print("\n")
    # for q in new_mtx:
    #     print(q)
    # print(len(mtx), len(mtx[0]), " ====> ", len(new_mtx), len(new_mtx[0]))

    return new_mtx


g = 18
print_patterns(patterns, g)
print("\n")
gm = transp(patterns[g - 1])
for tg in gm:
    print(tg)
# print(find_vert_LOR(patterns[0], True))
print(find_hori_LOR(patterns[g - 1], True))
print(find_hori_LOR(transp(patterns[g - 1]), True))

def P1(patterns):
    tot = 0
    for p in patterns:
        # print(find_hori_LOR(p, False), find_hori_LOR(transp(p), False))
        tot += (100 * find_hori_LOR(p, False)) + find_hori_LOR(transp(p), False)
    print("P1: ", tot)

P1(patterns)