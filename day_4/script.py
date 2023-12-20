inp = open('input').readlines()

total = 0

card_wins = []
propatagate = []

for card in inp:
    number_of_matches = 0

    cardx = card.split(":")
    numbers = cardx[1]

    numbersx = numbers.split("|")
    winning_numbers = numbersx[0].split(" ")
    my_numbers = numbersx[1].split(" ")

    winning_numbers = filter(lambda x: x != "", winning_numbers)
    my_numbers = filter(lambda y: y != "", my_numbers)

    winning_numbers = list(map(lambda x: int(x), winning_numbers))
    my_numbers = list(map(lambda y: int(y), my_numbers))

    points = 0

    for a in my_numbers:
        for b in winning_numbers:
            if (a == b):
                number_of_matches += 1
                if (points == 0):
                    points = 1
                else:
                    points *= 2
    total += points

    card_wins.append(number_of_matches)
    propatagate.append(1)

print(total)

for idx, multipler in enumerate(card_wins):
    for ix in range(multipler):
        if (idx + ix + 1) < len(card_wins):
            propatagate[idx + ix + 1] += propatagate[idx]
            print(list(card_wins[0:40]))
            print(list(propatagate[0:40]))


card_total = 0

for x in propatagate:
    card_total += x

print(card_total,"   ---")