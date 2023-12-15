inp = open('input').readlines()

total = 0

for card in inp:
    print(card)

    cardx = card.split(":")
    numbers = cardx[1]

    numbersx = numbers.split("|")
    winning_numbers = numbersx[0].split(" ")
    my_numbers = numbersx[1].split(" ")

    winning_numbers = filter(lambda x: x != "", winning_numbers)
    my_numbers = filter(lambda y: y != "", my_numbers)

    winning_numbers = list(map(lambda x: int(x), winning_numbers))
    my_numbers = list(map(lambda y: int(y), my_numbers))

    print("winning: ", list(winning_numbers))
    print("my_numbers: ", list(my_numbers))

    points = 0

    for a in my_numbers:
        for b in winning_numbers:
            if (a == b):
                print("Found a winning number: ", a)
                if (points == 0):
                    points = 1
                else:
                    points *= 2
    
    print("Value of this card is: ", points, "\n---\n")
    total += points

print(total)