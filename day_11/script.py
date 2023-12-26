inp = open("input").readlines()

g_map = []

def make_map(lines):
    g_map = []
    for l in lines:
        g_map.append(list(filter(lambda x : x != "\n", list(l))))
    return g_map

def expand_map(m):
    emptyRows = []
    emptyCols = []

    for r in range(len(m)):
        isEmptyRow = True
        for c in range(len(m[r])):
            if m[r][c] != ".":
                isEmptyRow = False
        if isEmptyRow:
            emptyRows.append(r)

    for c in range(len(m[0])):
        isEmptyCol = True
        for r in range(len(m)):
            if m[r][c] != ".":
                isEmptyCol = False
        if isEmptyCol:
            emptyCols.append(c)

    for er in reversed(emptyRows):
        m.insert(er, list(m[er][:]))
    
    for r in range(len(m)):
        for ec in reversed(emptyCols):
            m[r].insert(ec, ".")
    m[0][0]="A"
    return m

def grab_galaxies(m):
    galaxies = []
    # print(m)
    for r in range(len(m)):
        for c in range(len(m[r])):
            if (m[r][c] == "#"):
                galaxies.append((r,c))
    
    return galaxies

def dist_btwn_galaxies(gs, i, j):
    a = gs[i][0] - gs[j][0] if (gs[i][0] > gs[j][0]) else gs[j][0] - gs[i][0]
    b = gs[i][1] - gs[j][1] if (gs[i][1] > gs[j][1]) else gs[j][1] - gs[i][1]
    return a + b

g_map = make_map(inp)
print("\n".join(["".join(x) for x in g_map]))
e_map = expand_map(g_map)
print("\n".join(["".join(x) for x in e_map]))
galaxies = grab_galaxies(e_map)
print(galaxies)

total = 0
for (i, x) in enumerate(galaxies):
    for (j,y) in enumerate(galaxies):
        if (j > i):
            total += dist_btwn_galaxies(galaxies, i, j)

print("P1: ", total)