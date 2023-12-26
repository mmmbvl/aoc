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

moveSet = [
    [s[0] + 1, s[1]],
    [s[0] - 1, s[1]],
    [s[0], s[1] + 1],
    [s[0], s[1] - 1]
]

maxPathLength = 0

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
            curr = ans[0]
            next = ans[1]
        else:
            isLoop = False
            print("not a loop")
            break
    
    if (isLoop):
        print("Reached beginning again!! pathlength was: ", pathlength)
        if pathlength > maxPathLength:
            maxPathLength = pathlength

farthestDist = 0
if (maxPathLength % 2 == 0):
    farthestDist = 1 + maxPathLength / 2
else:
    farthestDist = 1 + (maxPathLength - 1) / 2
print("P1: ", farthestDist)