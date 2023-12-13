inp = open('input').readlines()

tot = 0
for line in inp:
    print("Processing line:")
    print(line)
    lt = 0
    for a in line:
        if (a.isdigit()):
            lt = lt + (int(a) * 10)
            print("Found first digit as ", a)
            break
    for a in reversed(line):
        if (a.isdigit()):
            lt = lt + (int(a))
            print("Found last digit as ", a)
            break
    tot = lt + tot
print(tot)


searchlist = {
    "one":      "1",
    "two":      "2",
    "three":    "3",
    "four":     "4",
    "five":     "5",
    "six":      "6",
    "seven":    "7",
    "eight":    "8",
    "nine":     "9",
    "zero":     "0",
    "3":        "3",
    "1":        "1",
    "2":        "2",
    "4":        "4",
    "5":        "5",
    "6":        "6",
    "7":        "7",
    "8":        "8",
    "9":        "9",
    "0":        "0"
}
# tot = 0
# for line in inp:
#     lt = 0
#     print("Processing line:")
#     print(line)
#     for tm in searchlist:
#         line = line.replace(tm, searchlist[tm])
#     print(line)
#     for a in line:
#         if (a.isdigit()):
#             lt = lt + (int(a) * 10)
#             print("Found first digit as ", a)
#             break
#     for a in reversed(line):
#         if (a.isdigit()):
#             lt = lt + (int(a))
#             print("Found last digit as ", a)
#             break
#     tot = lt + tot
# print(tot)

tot = 0
for line in inp:
    found = False
    print("processing: ", line)
    for i in range(0, len(line)):
        if (found):
            break
        for k in searchlist:
            if (i + len(k) <= len(line)):
                if (line[i:i+len(k)] in searchlist):
                    print("in searchList:  ", line[i:i+len(k)])
                    tot = tot + (int(searchlist[line[i:i+len(k)]]) * 10)
                    print("adding: ", int(searchlist[line[i:i+len(k)]]), " * 10")
                    found = True
                    break
    found = False
    for i in range(len(line), -1, -1):
        if (found):
            break
        for k in searchlist:
            if (i + len(k) <= len(line)):
                if (searchlist.get(line[i:i+len(k)]) != None):
                    tot = tot + (int(searchlist[line[i:i+len(k)]]) * 1)
                    print("adding: ", int(searchlist[line[i:i+len(k)]]))
                    found = True
                    break
print(tot)