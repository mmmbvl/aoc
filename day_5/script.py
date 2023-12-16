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
for line in inp:
    if (c == 0):
        seeds = line.split(" ")[1:]
        continue
    if (len(line) == 1):
        continue

    if line[0].isalpha() and c == 0:
        #map start
        map_name = line.split(" ")[0].split("-")
        start_v = map_name[0]
        end_v = map_name[2]
        continue

    map_d = line.split(" ")
    destn = map_d[0]
    sourc = map_d[1]
    rng_l = map_d[2]


