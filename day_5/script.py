inp = open('input').readlines()

items = [#"seed"       , 
         "soil"       , 
         "fertilizer" , 
         "water"      , 
         "light"      , 
         "temperature", 
         "humidity"   , 
         "location"
         ]


seedsData = list(map(lambda x: int(x), inp[0].split(" ")[1:]))
seeds = []
for i, x in enumerate(seedsData):
    if (i % 2 == 0):
        seeds.append([x])
    else:
        seeds[-1].append(x)
    # seeds = [
    #   ...
    #   [start, range]
    #   ...
    # ]

maps = {}
lineCount = 0
currMap = ""
for line in inp:
    if (lineCount == 0):
        lineCount += 1
        continue

    if (len(line) == 1): # empty line
        continue

    if line[0].isalpha():
        #map start
        map_name = line.split(" ")[0].split("-")
        start_v = map_name[0]
        end_v = map_name[2]
        currMap = end_v
        maps[end_v] = []
        continue
    
    lineCount += 1
    map_d = line.split(" ")
    destn = int(map_d[0])
    sourc = int(map_d[1])
    rng_l = int(map_d[2])

    maps[currMap].append([destn, sourc, rng_l])

for convTarget in items:
    for seedRange in seeds:
        # print(convTarget, " ---- ", maps["soil"])
        for convRange in maps[convTarget]:

            s_pt = seedRange[0]
            e_pt = seedRange[0] + seedRange[1] - 1

            conversion_destination_point = convRange[0]
            cv_s_pt = convRange[1]
            cv_e_pt = convRange[1] + convRange[2] - 1

            if e_pt < cv_s_pt:
                # below range
                continue
            if s_pt > cv_e_pt:
                # above range
                continue
            if s_pt >= cv_s_pt and e_pt <= cv_e_pt:
                offset = s_pt - cv_s_pt
                seedRange[0] = conversion_destination_point + offset
                continue
            if s_pt < cv_s_pt and e_pt >= cv_s_pt and e_pt <= cv_e_pt:
                # start below, run into
                # cut:
                new_s_pt = s_pt
                new_e_pt = cv_s_pt - 1
                seeds.append([new_s_pt, new_e_pt - new_s_pt + 1])

                #reform:
                s_pt = cv_s_pt
                seedRange[0] = s_pt
                seedRange[1] = e_pt - s_pt + 1
                offset = s_pt - cv_s_pt
                seedRange[0] = conversion_destination_point + offset
                continue
            if s_pt >= cv_s_pt and s_pt <= cv_e_pt and e_pt > cv_e_pt:
                # start within, run out
                #cut:
                new_s_pt = cv_e_pt + 1
                new_e_pt = e_pt
                seeds.append([new_s_pt, new_e_pt - new_s_pt + 1])

                #reform:
                e_pt = cv_e_pt
                seedRange[0] = s_pt
                seedRange[1] = e_pt - s_pt + 1
                offset = s_pt - cv_s_pt
                seedRange[0] = conversion_destination_point + offset
                continue
            if s_pt < cv_s_pt and e_pt > cv_e_pt:
                # start under, end over
                #cut1:
                new_s_pt = s_pt
                new_e_pt = cv_s_pt - 1
                seeds.append([new_s_pt, new_e_pt - new_s_pt + 1])

                #cut2:
                new_s_pt = cv_e_pt + 1
                new_e_pt = e_pt
                seeds.append([new_s_pt, new_e_pt - new_s_pt + 1])

                #reform:
                s_pt = cv_s_pt
                e_pt = cv_e_pt
                seedRange[0] = s_pt
                seedRange[1] = e_pt - s_pt + 1
                offset = s_pt - cv_s_pt
                seedRange[0] = conversion_destination_point + offset
                continue










# for convTarget in items:
#     for seedRange in seeds:
#         # print(convTarget, " ---- ", maps["soil"])
#         for convRange in maps[convTarget]:

#             initial_point = seedRange[0]
#             initial_length = seedRange[1]

#             conversion_destination_point = convRange[0]
#             conversion_source_point = convRange[1]
#             conversion_length = convRange[2]
#             print("\n\nComparing these: ")
#             print("Initial at:                               ", initial_point, "----    ", initial_length)
#             print("against:     ", "dest:", conversion_destination_point, "----","src:  ",conversion_source_point,"----","rng:",conversion_length)
#             if initial_point < conversion_source_point and initial_point + initial_length < conversion_source_point + conversion_length:
#                 print("below range - skip")
#                 continue
#             elif initial_point > conversion_source_point + conversion_length:
#                 print("above range - skip")
#                 continue
#             elif initial_point >= conversion_source_point and initial_point + initial_length <= conversion_source_point + conversion_length:
#                 print("within range")
#                 conv_offset = initial_point - conversion_source_point
#                 initial_point = conversion_destination_point + conv_offset
#             elif initial_point >= conversion_source_point and initial_point + initial_length > conversion_source_point + conversion_length:
#                 # starts in conversion range, but extends beyond -- must split
#                 print("start within, end out")
#                 new_point = conversion_source_point + conversion_length + 1
#                 new_length = initial_point + initial_length - new_point + 1
#                 seeds.append([new_point, new_length])
#                 print("created new split:    ", new_point, "----", new_length)

#                 initial_length = conversion_source_point + conversion_length - initial_point + 1

#                 conv_offset = initial_point - conversion_source_point
#                 initial_point = conversion_destination_point + conv_offset
#             elif initial_point < conversion_source_point and initial_point + initial_length <= conversion_source_point + conversion_length:
#                 # starts before conversion range, but ends within
#                 print("start out, end in")
#                 new_point = initial_point
#                 new_length = conversion_source_point - initial_point
#                 seeds.append([new_point, new_length])
#                 print("created new split:    ", new_point, "----", new_length)

#                 initial_length = initial_point + initial_length - conversion_source_point + 1
#                 initial_point = conversion_source_point

#                 conv_offset = initial_point - conversion_source_point
#                 initial_point = conversion_destination_point + conv_offset
#             elif initial_point < conversion_source_point and initial_point + initial_length > conversion_source_point + conversion_length:
#                 # starts before conversion range, ends after conversion range -- must split twice
#                 print("run all through")
#                 new_point = conversion_source_point + conversion_length + 1
#                 new_length = initial_point + initial_length - new_point + 1
#                 seeds.append([new_point, new_length])
#                 print("created new split:    ", new_point, "----", new_length)

#                 new_point = initial_point
#                 new_length = conversion_source_point - initial_point
#                 seeds.append([new_point, new_length])
#                 print("created new split:    ", new_point, "----", new_length)

#                 initial_point = conversion_destination_point
#                 initial_length = conversion_length
            
#             seedRange[0] = initial_point
#             seedRange[1] = initial_length
#             # print("Comparing these: ")
#             print("Result at:  ", initial_point, "----", initial_length)
#             # print("against:     ", "dest:", conversion_destination_point, "----","src:",conversion_source_point,"----","rng:",conversion_length)


# find lowest
minVal = seeds[0][0]
for seedRange in seeds:
    if minVal > seedRange[0]:
        minVal = seedRange[0]

print("the minimum value you are looking for is ", minVal)

# c = 0
# seeds = []
# seedschanged = []
# current_v = "seed"

# print("Initializing...")
# seeds = list(map(lambda x: int(x), inp[0].split(" ")[1:]))
# seedschanged = seeds[:]
# for yyy, zzz in enumerate(seedschanged):
#     seedschanged[yyy] = False
# print("seeds: ", list(seeds))
# print("change status: ", list(seedschanged), "\n\n---\n\n")



# #seed ranges
# seedslist = list(map(lambda x: int(x), inp[0].split(" ")[1:]))
# stpt = -1
# rngpt = -1
# for item in seedslist:
#     if (stpt == -1):
#         stpt = item
#         continue
#     rngpt = item
#     seeds += list(range(stpt, stpt + rngpt))
#     stpt = -1
#     rngpt = -1

# for uy, uc in enumerate(seeds):
#     if (uy % 921119 != 0):
#         seeds[uy:uy+1] = []

# seedschanged = seeds[:]
# for yyy, zzz in enumerate(seedschanged):
#     seedschanged[yyy] = False


# for line in inp:
#     # if (c == 0):
#     #     print("Initializing...")
#     #     seeds = map(lambda x: int(x), line.split(" ")[1:])
#     #     seedschanged = line.split(" ")[1:]
#     #     for yyy, zzz in enumerate(seedschanged):
#     #         seedschanged[yyy] = False
#     #     print("seeds: ", list(seeds))
#     #     print("change status: ", list(seedschanged), "\n\n---\n\n")
#     #     c += 1
#     #     continue

#     if (c == 0):
#         c += 1
#         continue

#     if (len(line) == 1):
#         continue

#     if line[0].isalpha():
#         #map start
#         for yyy, zzz in enumerate(seedschanged):
#             seedschanged[yyy] = False
#         map_name = line.split(" ")[0].split("-")
#         start_v = map_name[0]
#         end_v = map_name[2]
#         current_v = end_v
#         print("Found a map: ", start_v, " to ", end_v, " ---###--- ", line)
#         continue
    
#     c += 1
#     map_d = line.split(" ")
#     destn = int(map_d[0])
#     sourc = int(map_d[1])
#     rng_l = int(map_d[2])

#     print("Info from this map: ", "destn=", destn, "   ---   sourc=", sourc, "   ---   rng_l=", rng_l)

#     for x, y in enumerate(seeds):
#         s = int(y)
#         if (s >= sourc and s < sourc + rng_l) and not seedschanged[x]:
#            print(seeds[x])
#            seeds[x] = destn + s - sourc
#            seedschanged[x] = True

#     print("Updates based on info: ")
#     print("seeds: ", list(seeds))
#     print("change status: ", list(seedschanged[0:10]), "\n---\n")

# print(list(seeds))
# print(min(list(seeds)))
