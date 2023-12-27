inp = open("input").readlines()

g_map = []

def make_map(lines):
    g_map = []
    for l in lines:
        g_map.append(list(filter(lambda x : x != "\n", list(l))))
    return g_map

def expand_map(m, expansion_factor):
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
        for z in range(expansion_factor):
            m.insert(er, list(m[er][:]))
    
    for r in range(len(m)):
        for ec in reversed(emptyCols):
            for z in range(expansion_factor):
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
e_map = expand_map(g_map, 1)
print("\n".join(["".join(x) for x in e_map]))
galaxies = grab_galaxies(e_map)
print(galaxies)

total = 0
for (i, x) in enumerate(galaxies):
    for (j,y) in enumerate(galaxies):
        if (j > i):
            total += dist_btwn_galaxies(galaxies, i, j)

print("P1: ", total)






def discover_empty_rows(m):
    emptyRows = []
    for r in range(len(m)):
        isEmptyRow = True
        for c in range(len(m[r])):
            if m[r][c] != ".":
                isEmptyRow = False
        if isEmptyRow:
            emptyRows.append(r)
    return emptyRows

def discover_empty_cols(m):
    emptyCols = []
    for c in range(len(m[0])):
        isEmptyCol = True
        for r in range(len(m)):
            if m[r][c] != ".":
                isEmptyCol = False
        if isEmptyCol:
            emptyCols.append(c)
    return emptyCols

def compensated_dist_btwn_galaxies(gs, i, j, e_rows, e_cols):
    a = gs[i][0] - gs[j][0] if (gs[i][0] > gs[j][0]) else gs[j][0] - gs[i][0]
    b = gs[i][1] - gs[j][1] if (gs[i][1] > gs[j][1]) else gs[j][1] - gs[i][1]

    for e_row in e_rows:
        if (gs[i][0] < e_row and gs[j][0] > e_row) or (gs[i][0] > e_row and gs[j][0] < e_row):
            a += 1000000 - 1

    
    for e_col in e_cols:
        if (gs[i][1] < e_col and gs[j][1] > e_col) or (gs[i][1] > e_col and gs[j][1] < e_col):
            b += 1000000 - 1

    return a + b

g_map = make_map(inp)
# print("\n".join(["".join(x) for x in g_map]))
e_rows = discover_empty_rows(g_map)
e_cols = discover_empty_cols(g_map)

print(e_rows)
# print("\n".join(["".join(x) for x in e_map]))
galaxies = grab_galaxies(g_map)
# print(galaxies)


total = 0
for (i, x) in enumerate(galaxies):
    for (j,y) in enumerate(galaxies):
        if (j > i):
            total += compensated_dist_btwn_galaxies(galaxies, i, j, e_rows, e_cols)

print("P2: ", total)