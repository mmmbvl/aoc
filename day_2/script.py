inp = open('input').readlines()

MAXIMUMS = {
    "red":      12,
    "blue":     14,
    "green":    13
}

total = 0
for game in inp:
    print("Looking at Game: ", game)
    rounds = game.split(":")[1]

    isValid = True
    for round in rounds.split(";"):
        print("Looking at Round: ", round)
        colors = round.split(", ")
        for color in colors:
            print("Looking at color: ", color)
            number_found = int("".join(filter(lambda n: n.isdigit(), list(color))))
            print("The number found was: ", number_found)
            color_found = "".join(filter(lambda n: n.isalpha(), list(color)))
            print("The color found was: ", color_found)
            for limit in MAXIMUMS:
                if not (color_found in MAXIMUMS.keys()) or (number_found > MAXIMUMS[color_found]):
                    isValid = False
    if isValid:
        game_number = int("".join(filter(lambda n: n.isdigit(), list(game.split(":")[0]))))
        total += game_number

print("Total is: ", total)