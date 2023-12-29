inp = open("input").readlines()

symbol_data = []
number_data = []

for line in inp:
    a = line.split(" ")
    symbol_data.append(list(a[0]))
    number_data.append(list(map(lambda x : int(x), a[1].split(","))))

def attempt_placement(symbols, last_placed, sz):
    valid_placements = []
    # print("Attempting placement into: ")
    # print(symbols)
    
    dbg_arr = ["." for x in range(len(symbols) + sz + 1)]
    terminal = False

    for i in range(len(symbols)):
        if i < last_placed:
            continue
        # dbg_arr = ["." for x in range(len(symbols) + sz + 1)]
        # dbg_arr[i] = "^"
        # dbg_arr[i + sz + 1] = "^"
        
        valid = True
        if symbols[i] == "#":
            # dbg_arr[i] = ":"
            terminal = True
            valid = False
            break
        for a in range(sz):
            if (i + a + 1 >= len(symbols)) or symbols[i + a + 1] == ".":
                # dbg_arr[i + a + 1] = "X"
                valid = False
            else:
                v = 0
                dbg_arr[i + a + 1] = "O"
        if (i + sz + 1 < len(symbols)) and symbols[i + sz + 1] == "#":
            # dbg_arr[i + sz + 1] = ":"
            valid = False
        
        # print(dbg_arr, " ------> ", valid)

        if valid:
            valid_placements.append(i + sz + 1)
    
    # print("                                                 Terminal is: ", terminal)
    # print("Result: ", valid_placements)
    return valid_placements

def place_all(symbs, numbs):
    # print("---place_all:            ", symbs, numbs)
    # print("---place_all:   prefix   ", symbs, numbs)
    symbs.insert(0,".")
    endpoints = [0]
    possibilities_tracker = {0: 1}

    for i, n in enumerate(numbs):
        next_stage_possibles = {}
        purified_n_ep = set()

        for ep in endpoints:
            next_endpoints = attempt_placement(symbs,ep,n)
            for n_ep in next_endpoints:
                purified_n_ep.add(n_ep)
                if not n_ep in next_stage_possibles:
                    next_stage_possibles[n_ep] = 0
                next_stage_possibles[n_ep] += possibilities_tracker[ep]
    
        endpoints = list(purified_n_ep)
        possibilities_tracker = next_stage_possibles

    last_spring = 0
    for i in reversed(range(len(symbs))):
        if symbs[i] == "#":
            last_spring = i
            break

    tot = 0
    for ep in possibilities_tracker:
        if ep >= last_spring:
            tot += possibilities_tracker[ep]

    return tot


#     # print("---place_all:            ", symbs, numbs)
#     collector = 0
#     symbs.insert(0,".")
#     # print("---place_all:   prefix   ", symbs, numbs)
#     valid_stk = [0]
#     wallis = [[0]]
#     for i,n in enumerate(numbs):
#         next_stage_stacks = set()
#         all_found = []
#         for lp in valid_stk:
#             ans = attempt_placement(symbs, lp, n)
#             all_found += ans
           
#             collector += len(all_found)
#             for hjk in all_found:
#                 next_stage_stacks.add(hjk)
#             # for wls in wallis:
#             #     if wls[-1] == lp:
#             #         wallis.append(wls + list(next_stage_stacks)) 
#             # # if i == len(numbs) - 1:
#             #     lastx = 0
#             #     for tr in reversed(range(len(symbs))):
#             #         if symbs[tr] == "#":
#             #             lastx = tr
#             #             break       
#             #     if len(next_stage_stacks) > 0 and next_stage_stacks[-1] <= lastx:
#             #         next_stage_stacks.pop()
#         valid_stk = list(next_stage_stacks)

#     # print("Cleaning up: ", valid_stk)
#     # ab = set()
#     # for hh in valid_stk:
#     #     ab.add(hh)
#     # valid_stk = list(ab)

#     lastx = 0
#     for tr in reversed(range(len(symbs))):
#         if symbs[tr] == "#":
#             lastx = tr
#             break       

#     wallis = list(filter(lambda x : len(x) == len(numbs) + 1, wallis))

#     removes = set()
#     for i,n in enumerate(valid_stk):
#         # for j,z in enumerate(symbs):
#             if n < lastx:
#             # if j > n and symbs[j] == "#":
#                 removes.add(i)
#     # print("Following are invalid: ", list(removes))
#     # print(removes)#, valid_stk)
#     # print(len(removes), len(valid_stk))
#     for k in reversed(sorted(list(removes))):
#         # print("pop",len(removes), len(valid_stk), " @ ", k)
#         valid_stk.pop(k)
#     # print("Cleaned up: ", valid_stk)
#    # print(removes)#, valid_stk)
#     # print(len(removes), len(valid_stk))
#     # print("---place_all:   result   ", len(valid_stk), symbs, numbs)
#     return len(valid_stk) + collector

total = 0
for i in range(len(symbol_data)):
# for i in range(1): #range(len(symbol_data)):
    total += place_all(symbol_data[i], number_data[i])

print("P1: ", total)




def unfolding_symbols(syms):
    new_s_data = []
    for s in syms:
        new_s = [] + s
        for f in range(4):
            new_s += ["?"]
            new_s += s
        new_s_data.append(new_s)
    return new_s_data

def unfolding_numbers(nums):
    new_n_data = []
    for n in nums:
        new_n = [] + n
        for f in range(4):
            new_n += n
        new_n_data.append(new_n)
    return new_n_data

# print("Unfolding: ")
# print(symbol_data[1])
# print(unfolding_symbols(symbol_data)[1])
# print(number_data[1])
# print(unfolding_numbers(number_data)[1])

total = 0
ccs = unfolding_symbols(symbol_data)
ccn = unfolding_numbers(number_data)
limiter = [0,1000]
for i in range(len(ccs)):
# for i in range(1): #range(len(symbol_data)):
# for i in range(limiter[0],limiter[1]):
    total += place_all(ccs[i], ccn[i])

print("P2: up to ",limiter," === ", total)