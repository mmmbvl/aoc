inp = open('input').readlines()

MAXIMUMS = {
    "red":      12,
    "blue":     14,
    "green":    13
}

total = 0
for game in inp:
    # print("Looking at Game: ", game)
    rounds = game.split(":")[1]

    isValid = True
    for round in rounds.split(";"):
        # print("Looking at Round: ", round)
        colors = round.split(", ")
        for color in colors:
            # print("Looking at color: ", color)
            number_found = int("".join(filter(lambda n: n.isdigit(), list(color))))
            # print("The number found was: ", number_found)
            color_found = "".join(filter(lambda n: n.isalpha(), list(color)))
            # print("The color found was: ", color_found)
            for limit in MAXIMUMS:
                if not (color_found in MAXIMUMS.keys()) or (number_found > MAXIMUMS[color_found]):
                    isValid = False
    if isValid:
        game_number = int("".join(filter(lambda n: n.isdigit(), list(game.split(":")[0]))))
        total += game_number

# print("Total is: ", total)



total = 0
for game in inp:
    # print("Looking at Game: ", game)
    rounds = game.split(":")[1]

    colors_req = {}

    for round in rounds.split(";"):
        colors = round.split(", ")
        for color in colors:
            number_found = int("".join(filter(lambda n: n.isdigit(), list(color))))
            color_found = "".join(filter(lambda n: n.isalpha(), list(color)))
            if not (color_found in colors_req.keys()) or (number_found > colors_req[color_found]):
                colors_req[color_found] = number_found
    
    # print("Cubes required for this game are: ", colors_req)
    power = 1
    for c in colors_req:
        power *= colors_req[c]
    total += power


# print("Total is: ", total)