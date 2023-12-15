inp = open('input').readlines()

gears = {

}

def determineValidity(row, start, end, n):
    valid = False
    for r in range(row - 1, row + 2):
        if r >= 0 and r < len(ary):
            print("".join(ary[r]))
        for c in range(start - 1, end + 1):
            if (r >= 0) and (r < len(ary)) and (c >= 0) and (c < len(ary[r]) - 1):
                if not ary[r][c].isdigit() and not (ary[r][c] == "."):
                    if ary[r][c] == "*":
                        gear_location = str(r) + "-" + str(c)
                        if not (gear_location in gears):
                            gears[gear_location] = []
                        gears[gear_location].append(n)
                    valid = True
                    print("number is at ", start, " ", end, "---pinged valid at: ", r, " ", c)
    print("".join(ary[row][start:end]), " is ", valid)
    return valid

ary = []
for line in inp:
    ary.append(list(line))

total = 0
for rx, r in enumerate(ary):
    numixstart = -1
    numixend = -1
    for cx, c in enumerate(r):
        if (c.isdigit() and cx > numixend):
            p = cx
            numixstart = p
            while (p < len(r)) and r[p].isdigit():
                p += 1
            numixend = p
            number_found = int("".join(r[numixstart:numixend]))
            if determineValidity(rx, numixstart, numixend, number_found):
                total += number_found
                print("added ", number_found)

print(total)

gear_total = 0

print(gears)

for gear_num in gears:
    print(gears[gear_num], len(gears[gear_num]))
    if len(gears[gear_num]) == 2:
        gear_total += gears[gear_num][0] * gears[gear_num][1]

print(gear_total)