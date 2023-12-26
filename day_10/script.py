inp = open("input").readlines()


    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

m = []
s = []

for line in inp:
    r = list(line)
    m.append(r)
    # print(m)

for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c] == "S":
            s = [r, c]

def moveLoc(fr, to):
#     print("fr: ", fr, " == ", m[fr[0]][fr[1]], "@@@|||||||||@@@", "to: ", to, " == ", m[to[0]][to[1]])
    if (to[0] < 0) or (to[0] >= len(m)):
        return [fr, to, "invalid"]
    if (to[1] < 0) or (to[1] >= len(m[to[0]])):
        return [fr, to, "invalid"]

    tile = m[to[0]][to[1]]

    if tile == "|":
        if to[0] > fr[0]:
            return [to, [to[0] + 1, to[1]], "valid"]
        if to[0] < fr[0]:
            return [to, [to[0] - 1, to[1]], "valid"]
        return [fr, to, "invalid"]
    
    if tile == "-":
        if to[1] > fr[1]:
            return [to, [to[0], to[1] + 1], "valid"]
        if to[1] < fr[1]:
            return [to, [to[0], to[1] - 1], "valid"]
        return [fr, to, "invalid"]

    if tile == "L":
        if to[0] > fr[0]:
            return [to, [to[0], to[1] + 1], "valid"]
        if to[1] < fr[1]:
            return [to, [to[0] - 1, to[1]], "valid"]
        return [fr, to, "invalid"]

    if tile == "J":
        if to[0] > fr[0]:
            return [to, [to[0], to[1] - 1], "valid"]
        if to[1] > fr[1]:
            return [to, [to[0] - 1, to[1]], "valid"]
        return [fr, to, "invalid"]    

    if tile == "7":
        if to[0] < fr[0]:
            return [to, [to[0], to[1] - 1], "valid"]
        if to[1] > fr[1]:
            return [to, [to[0] + 1, to[1]], "valid"]
        return [fr, to, "invalid"]    
    
    if tile == "F":
        if to[0] < fr[0]:
            return [to, [to[0], to[1] + 1], "valid"]
        if to[1] < fr[1]:
            return [to, [to[0] + 1, to[1]], "valid"]
        return [fr, to, "invalid"]    
    
    if tile == ".":
        return [fr, to, "invalid"]    
    
    return [fr, to, "invalid"]

moveSet = [
    [s[0] + 1, s[1]],
    [s[0] - 1, s[1]],
    [s[0], s[1] + 1],
    [s[0], s[1] - 1]
]

maxPathLength = 0
pathNodes = []

def traverse(modify, mpl):
    for stDir in moveSet:
        curr = s
        next = stDir

        pathlength = 0
        isLoop = True

        while not (next[0] == s[0] and next[1] == s[1]):
            ans = moveLoc(curr, next)
            if pathlength < 10 or pathlength > 13560:
                print("fr: ", curr, " == ", m[curr[0]][curr[1]], "@@@|||||||||@@@", "to: ", next, " == ", m[next[0]][next[1]])
            if (ans[2] == "valid"):
                pathlength += 1
                pathNodes.append(next)
                if modify:
                    if (m[curr[0]][curr[1]] == "|"):
                        if next[0] > curr[0]:
                            m[curr[0]][curr[1]] = "H"
                        else:
                            m[curr[0]][curr[1]] = "N"
                    elif (m[curr[0]][curr[1]] == "-"):
                        if next[1] > curr[1]:
                            m[curr[0]][curr[1]] = "E"
                        else:
                            m[curr[0]][curr[1]] = "W"
                    elif (m[curr[0]][curr[1]] == "J"):
                        if next[0] < curr[0]:
                            m[curr[0]][curr[1]] = "n"
                        else:
                            m[curr[0]][curr[1]] = "s"
                    elif (m[curr[0]][curr[1]] == "7"):
                        if next[0] < curr[0]:
                            m[curr[0]][curr[1]] = "a"
                        else:
                            m[curr[0]][curr[1]] = "b"
                    elif (m[curr[0]][curr[1]] == "L"):
                        if next[0] < curr[0]:
                            m[curr[0]][curr[1]] = "c"
                        else:
                            m[curr[0]][curr[1]] = "d"
                    elif (m[curr[0]][curr[1]] == "F"):
                        if next[0] < curr[0]:
                            m[curr[0]][curr[1]] = "e"
                        else:
                            m[curr[0]][curr[1]] = "f"
                    else:
                        m[curr[0]][curr[1]] = "X"
                curr = ans[0]
                next = ans[1]
            else:
                isLoop = False
                print("not a loop")
                break
        
        if (isLoop):
            print("Reached beginning again!! pathlength was: ", pathlength)
            if pathlength > mpl:
                mpl = pathlength
    return mpl

maxPathLength = traverse(False, maxPathLength)
farthestDist = 0
if (maxPathLength % 2 == 0):
    farthestDist = 1 + maxPathLength / 2
else:
    farthestDist = 1 + (maxPathLength - 1) / 2
print("P1: ", farthestDist)


isInside = False
nses = set()
areaCounter = 0
for r in range(len(m)):
    for c in range(len(m[r])):
        inPath = False
        for pn in pathNodes:
            if r == pn[0] and c == pn[1]:
                inPath = True
        if inPath:
            if (m[r][c] in ["J", "|", "L"]):
                isInside = not isInside
            # else:
            #     isInside = False
        else:
            if isInside:
                areaCounter += 1
                nses.add((r,c))

print("P2 by toggle: ", areaCounter, "---", len(nses))

# maxPathLength = traverse(True, maxPathLength)
# print("\n\nModified State")
# for r in range(len(m)):
#     print("".join(m[r]))

# def pollute(m, pt, ctmt):
#     newPts = [
#         [pt[0] + 1,pt[1]],
#         [pt[0] - 1,pt[1]],
#         [pt[0],pt[1] + 1],
#         [pt[0],pt[1] - 1]
#         # [pt[0] + 1,pt[1] + 1],
#         # [pt[0] - 1,pt[1] - 1],
#         # [pt[0] - 1,pt[1] + 1],
#         # [pt[0] + 1,pt[1] - 1]
#     ]

#     b = m[pt[0]][pt[1]]
#     if not (b == "H" or b == "N" or b == "E" or b == "W" or b == "X" or b == ctmt):
#         m[pt[0]][pt[1]] = ctmt
#         for n in newPts:
#             if not (n[0] < 0 or n[1] < 0 or n[0] >= len(m) or n[1] >= len(m[n[0]])):
#                 b = m[n[0]][n[1]]
#                 if not (b == "H" or b == "N" or b == "E" or b == "W" or b == "X" or b == ctmt):
#                     pollute(m, n, ctmt)


# ttt = 0
# for r in range(len(m)):
#     for c in range(len(m[r])):
#         testedLoc = [r, c]
#         numEW_Walls = 0
#         numNS_Walls = 0
#         for cx in range(len(m[r])):
#             if cx != c:
#                 if m[r][cx] in ["N", "c", "d", "a", "b"]:
#                     numEW_Walls += 1
#         # for rx in range(len(m)):
#         #     if rx != r:
#         #         if m[rx][c] == "H" or m[rx][c] == "N":
#         #             numNS_Walls += 1
#         isWithin = (numEW_Walls % 2 == 1)# and (numNS_Walls % 2 == 1)
#         if (isWithin) and m[r][c] != "X":
#             ttt += 1

# print("Using wall counting method: ", ttt)


# # print("Pollute corner:")
# # pollute(m, [0,0], "*")
# # for r in range(len(m)):
# #     print("".join(m[r]))
                    

# # for r in range(len(m)):
# #     for c in range(len(m[r])):
# #         if m[r][c] == "E":
# #             pollute(m, [r - 1, c], "*")
# #         # if m[r][c] == "W":
# #         #     pollute(m, [r + 1, c], "*")
# #         # if m[r][c] == "N":
# #         #     pollute(m, [r, c - 1], "*")
# #         if m[r][c] == "H":
# #             pollute(m, [r, c + 1], "*")
# #         if m[r][c] == "n":
# #             pollute(m, [r - 1, c - 1], "*")

# # print("\n\nAssume loop c-clockwise: ")
# # for r in range(len(m)):
# #     print("".join(m[r]))

# area_find = 0
# for r in range(len(m)):
#     for c in range(len(m[r])):
#         if m[r][c] == "*":
#             area_find += 1
# print("P2: ", area_find)