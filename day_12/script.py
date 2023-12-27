inp = open("input").readlines()

symbol_data = []
number_data = []

for line in inp:
    a = line.split(" ")
    symbol_data.append(list(a[0]))
    number_data.append(list(map(lambda x : int(x), a[1].split(","))))

def attempt_placement(symbols, last_placed, sz):
    valid_placements = []
    print("Attempting placement into: ")
    print(symbols)
    
    # dbg_arr = ["." for x in range(len(symbols) + sz + 1)]
    terminal = False

    for i in range(len(symbols)):
        if i < last_placed:
            continue
        dbg_arr = ["." for x in range(len(symbols) + sz + 1)]
        dbg_arr[i] = "^"
        dbg_arr[i + sz + 1] = "^"
        
        valid = True
        if symbols[i] == "#":
            dbg_arr[i] = ":"
            terminal = True
            valid = False
            break
        for a in range(sz):
            if (i + a + 1 >= len(symbols)) or symbols[i + a + 1] == ".":
                dbg_arr[i + a + 1] = "X"
                valid = False
            else:
                dbg_arr[i + a + 1] = "O"
        if (i + sz + 1 < len(symbols)) and symbols[i + sz + 1] == "#":
            dbg_arr[i + sz + 1] = ":"
            valid = False
        
        print(dbg_arr, " ------> ", valid)

        if valid:
            valid_placements.append(i + sz + 1)
    
    print("                                                 Terminal is: ", terminal)
    print("Result: ", valid_placements)
    return valid_placements

def place_all(symbs, numbs):
    print("---place_all:            ", symbs, numbs)
    symbs.insert(0,".")
    print("---place_all:   prefix   ", symbs, numbs)
    valid_stk = [0]
    for i,n in enumerate(numbs):
        next_stage_stacks = []
        for lp in valid_stk:
            next_stage_stacks += attempt_placement(symbs, lp, n)       
        valid_stk = next_stage_stacks

    print("Cleaning up: ", valid_stk)
    removes = set()
    for i,n in enumerate(valid_stk):
        for j,z in enumerate(symbs):
            if j > n and symbs[j] == "#":
                removes.add(i)
    print("Following are invalid: ", list(removes))
    for k in reversed(list(removes)):
        valid_stk.pop(k)
    print("Cleaned up: ", valid_stk)

    print("---place_all:   result   ", len(valid_stk), symbs, numbs)
    return len(valid_stk)

total = 0
for i in range(len(symbol_data)):
# for i in range(1): #range(len(symbol_data)):
    total += place_all(symbol_data[i], number_data[i])

print("P1: ", total)