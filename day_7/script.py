inp = open("input").readlines()

hands = []
for line in inp:
    l = line.split(" ")
              #  (hand, bet  )
    hands.append([l[0], l[1]])

cardRanks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
def convertRank(card):
    for i,x in enumerate(cardRanks):
        if (card == x):
            return i
    return -1

handRanks = {
    1:"Five of a Kind",
    2:"Four of a Kind",
    3:"Full House",
    4:"Three of a Kind",
    5:"Two Pair"      ,
    6:"One Pair"     ,
    7:"High Card"
}

for h in hands:
    cards = list(h[0])
    cards_types = {}

    h.append(-1)
    for c in cards:
        if c not in cards_types:
            cards_types[c] = 0
        cards_types[c] += 1
    
    orderings = list(reversed(sorted(cards_types.values())))

    if orderings[0] == 5:
        h[2] = 1
    elif orderings[0] == 4:
        h[2] = 2
    elif orderings[0] == 3 and orderings[1] == 2:
        h[2] = 3
    elif orderings[0] == 3:
        h[2] = 4
    elif orderings[0] == 2 and orderings[1] == 2:
        h[2] = 5
    elif orderings[0] == 2:
        h[2] = 6
    else:
        h[2] = 7
    

    h.append(list(map(convertRank, cards)))

    # print("Processing the hand: ", h[0])
    # print("======> Hand:", handRanks[h[2]], "       ====   card ranks:", h[3])

def camelCardSort(hands):
    # hand: (cards) (bet) (handRank) (cardRanks[])
    s = hands
    # for j in reversed(range(5)):
    #     s = sorted(hands, key=lambda h: h[3][0])
    s = sorted(s, key=lambda h: h[3][4])
    s = sorted(s, key=lambda h: h[3][3])
    s = sorted(s, key=lambda h: h[3][2])
    s = sorted(s, key=lambda h: h[3][1])
    s = sorted(s, key=lambda h: h[3][0])
    s = sorted(s, key=lambda h: h[2])
    return s

sorted_hands = camelCardSort(hands)
# for i,g in enumerate(sorted_hands):
#     print(g, "  ", int(g[1]),"  ", (len(sorted_hands) - i))

value = 0
for i,g in enumerate(sorted_hands):
    value += int(g[1]) * (len(sorted_hands) - i)
print(value)




jokerCardRanks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
def convertJokerRank(card):
    for i,x in enumerate(jokerCardRanks):
        if (card == x):
            return i
    return -1

for h in hands:
    num_jokers = 0
    for x in list(h[0]):
        if x == "J":
            num_jokers += 1
    
    if h[2] == 2 and num_jokers > 0:
        h[2] = 1
    if h[2] == 3 and num_jokers > 0:
        h[2] = 1
    if h[2] == 4 and num_jokers > 0:
        h[2] = 2
    if h[2] == 5 and num_jokers == 1:
        h[2] = 3
    if h[2] == 5 and num_jokers == 2:
        h[2] = 2
    if h[2] == 6 and num_jokers > 0:
        h[2] = 4
    if h[2] == 7 and num_jokers > 0:
        h[2] = 6       

    
    h[3] = (list(map(convertJokerRank, h[0])))

sorted_hands = camelCardSort(hands)
for i,g in enumerate(sorted_hands):
    print(g, "  ", int(g[1]),"  ", (len(sorted_hands) - i))

value = 0
for i,g in enumerate(sorted_hands):
    value += int(g[1]) * (len(sorted_hands) - i)
print(value)