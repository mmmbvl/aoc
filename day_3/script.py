inp = open('input').readlines()


def determineValidity(row, start, end):
    valid = False
    for r in range(row - 1, row + 2):
        if r >= 0 and r < len(ary):
            print("".join(ary[r]))
        for c in range(start - 1, end + 1):
            if (r >= 0) and (r < len(ary)) and (c >= 0) and (c < len(ary[r]) - 1):
                if not ary[r][c].isdigit() and not (ary[r][c] == "."):
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
            if determineValidity(rx, numixstart, numixend):
                number_found = int("".join(r[numixstart:numixend]))
                total += number_found
                print("added ", number_found)

print(total)
