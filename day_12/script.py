inp = open("input").readlines()

marker_data = []
number_data = []

for line in inp:
    a = line.split(" ")
    marker_data.append(list(a[0]))
    number_data.append(list(map(lambda x : int(x), a[1].split(","))))

# print(marker_data, number_data)

def validate(symbols, numbers):
    print("Validating: ", symbols, "\n>Desired:                        ", numbers)
    g = []
    active = False
    count = 0
    for s in symbols:
        if s == "#" and active == False:
            active = True
            count += 1
        elif s == "#" and active == True:
            count += 1
        elif s == "." and active == True:
            active = False
            g.append(count)
            count = 0
        elif s == "." and active == False:
            continue
        else:
            return False
    
    print("Measured:                        ", g)

    if len(g) != len(numbers):
        return False
    
    for i, n in enumerate(numbers):
        if g[i] != numbers[i]:
            return False
    
    return True

def get_unknowns(symbols):
    unk = []
    for i,s in enumerate(symbols):
        if s == "?":
            unk.append(i)
    return unk

def possible_comb(unk_sym):
    print("545222-----------")
    pile = []
    pile.append(unk_sym)
    for i,x in enumerate(unk_sym):
        t = unk_sym[:]
        t[i] = "#"
        prefix = t[0:i+1]
        suffix = t[i+1:]
        # print("prefix:",prefix,"suffix:",suffix)
        new_suffixes = possible_comb(suffix)
        for new_suffix in new_suffixes:
            new_t = prefix + new_suffix
            pile.append(new_t)
    return pile
# lkp = {}
# for i in range(25):
#     lkp[i] = possible_comb(["." for c in range(i)])

def num_possible_combinations(symbols, numbers):
    unk = get_unknowns(symbols)
    total_valid = 0
    pwk = symbols[:]

    blank = []
    for e in unk:
        blank.append(".")
    
    all_filler_possibles = possible_comb(blank)
    # all_filler_possibles = lkp[len(blank)]

    # for n in all_filler_possibles:
    #     print(n)

    for p, filler_possible in enumerate(all_filler_possibles):
        for i,fp in enumerate(filler_possible):
            pwk[unk[i]] = fp
        print("\n\nFilling in: ", symbols, "( ",p, " of ",len(all_filler_possibles)," )")
        if validate(pwk, numbers):
            print("========> Valid")
            total_valid += 1
        else:
            print("========> Invalid")
    
    return total_valid

total = 0
for i, s in enumerate(marker_data):
    total += num_possible_combinations(marker_data[i], number_data[i])

print("P1: ", total)