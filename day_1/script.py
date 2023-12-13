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