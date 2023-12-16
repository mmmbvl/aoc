inp = open('input').readlines()

items = ["seed"       , 
         "soil"       , 
         "fertilizer" , 
         "water"      , 
         "light"      , 
         "temperature", 
         "humidity"   , 
         "location"
         ]

c = 0
seeds = []
seedschanged = []
current_v = "seed"

print("Initializing...")
seeds = list(map(lambda x: int(x), inp[0].split(" ")[1:]))
seedschanged = seeds[:]
for yyy, zzz in enumerate(seedschanged):
    seedschanged[yyy] = False
print("seeds: ", list(seeds))
print("change status: ", list(seedschanged), "\n\n---\n\n")



#seed ranges
seedslist = list(map(lambda x: int(x), inp[0].split(" ")[1:]))
stpt = -1
rngpt = -1
for item in seedslist:
    if (stpt == -1):
        stpt = item
        continue
    rngpt = item
    seeds += list(range(stpt, stpt + rngpt))
    stpt = -1
    rngpt = -1

for uy, uc in enumerate(seeds):
    if (uy % 921119 != 0):
        seeds[uy:uy+1] = []

seedschanged = seeds[:]
for yyy, zzz in enumerate(seedschanged):
    seedschanged[yyy] = False


for line in inp:
    # if (c == 0):
    #     print("Initializing...")
    #     seeds = map(lambda x: int(x), line.split(" ")[1:])
    #     seedschanged = line.split(" ")[1:]
    #     for yyy, zzz in enumerate(seedschanged):
    #         seedschanged[yyy] = False
    #     print("seeds: ", list(seeds))
    #     print("change status: ", list(seedschanged), "\n\n---\n\n")
    #     c += 1
    #     continue
    if (c == 0):
        c += 1
        continue

    if (len(line) == 1):
        continue

    if line[0].isalpha():
        #map start
        for yyy, zzz in enumerate(seedschanged):
            seedschanged[yyy] = False
        map_name = line.split(" ")[0].split("-")
        start_v = map_name[0]
        end_v = map_name[2]
        current_v = end_v
        print("Found a map: ", start_v, " to ", end_v, " ---###--- ", line)
        continue
    
    c += 1
    map_d = line.split(" ")
    destn = int(map_d[0])
    sourc = int(map_d[1])
    rng_l = int(map_d[2])

    print("Info from this map: ", "destn=", destn, "   ---   sourc=", sourc, "   ---   rng_l=", rng_l)

    for x, y in enumerate(seeds):
        s = int(y)
        if (s >= sourc and s < sourc + rng_l) and not seedschanged[x]:
           print(seeds[x])
           seeds[x] = destn + s - sourc
           seedschanged[x] = True

    print("Updates based on info: ")
    print("seeds: ", list(seeds))
    print("change status: ", list(seedschanged[0:10]), "\n---\n")

print(list(seeds))
print(min(list(seeds)))
