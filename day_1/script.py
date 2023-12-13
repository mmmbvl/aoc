inp = open('input').readlines()

tot = 0
for line in inp:
    lt = 0
    for a in line:
        if (a.isdigit()):
            lt = lt + (int(a) * 10)
    for a in line:
        b = 0
        if (a.isdigit()):
            lt = lt + int(a)
            lt = lt - int(b)
            b = int(a)
    tot = lt + tot
print(tot)