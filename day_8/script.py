inp = open("input").readlines()

instructions = inp[0][0:-1]

pathing = {}
current_loc = "AAA"
num_steps = 0

for i, line in enumerate(inp):
    if i < 2:
        continue
    
    l = line.split(" = ")
    d = l[1][1:-2].split(", ")

    start = l[0]
    left = d[0]
    right = d[1]

    pathing[start] = (left, right)

    # if i == 2:
    #     current_loc = start

# for g in pathing:
#     print(g, pathing[g])

while current_loc != "ZZZ":
    dir = list(instructions)[num_steps % len(instructions)]
    # print("At: ", current_loc, pathing[current_loc])
    # print("Direction is: ", dir)


    num_steps += 1
    if dir == "L":
        current_loc = pathing[current_loc][0]
    if dir == "R":
        current_loc = pathing[current_loc][1]

    # print("Now went to: ", current_loc)       

print(num_steps)

