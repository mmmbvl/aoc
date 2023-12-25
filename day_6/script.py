inp = open('input').readlines()


def distTravelled(maxTime, pushButtonTime):
    # print("Calculating distTravelled: ", "maxTime: ", maxTime, " and  pushButtonTime: ", pushButtonTime, " ---->    ", pushButtonTime * (maxTime - pushButtonTime))
    return pushButtonTime * (maxTime - pushButtonTime)

raceTimes = list(map(lambda x : int(x), filter(lambda x : x != "", inp[0].split(" ")[1:])))
print("Race times are: ", list(raceTimes))

winDistances = list(map(lambda x : int(x), filter(lambda x : x != "", inp[1].split(" ")[1:])))
print("Race times are: ", list(winDistances))


P1 = 1
print("\n\nPart 1-------------")
print(list(raceTimes))
print(list(enumerate(raceTimes)))
for (i, max_time) in enumerate(raceTimes):
    spacer = 0
    for x in range(max_time):
        # print(x)
        if distTravelled(max_time, x) > winDistances[i]:
            spacer = x
            break
    
    min_pbt = spacer
    max_pbt = max_time - spacer

    all_possible_for_race = max_pbt - min_pbt + 1

    P1 = P1 * all_possible_for_race
    print("For race: ", "race time is ", raceTimes[i], " with distance record ", winDistances[i])
    print("... the minimum winning PBT would be ", spacer)
    print("..& the maximum winning PBT would be ", max_time - spacer)
print(P1)


print("\n\nPart 2-------------")
wholeRaceTime = int("".join(list(map(lambda x : str(x), raceTimes))))
print("The whole race time is ", wholeRaceTime)
wholeDistRecord = int("".join(list(map(lambda x : str(x), winDistances))))
print("The whole dist record is ", wholeDistRecord)
P2 = 0
spacer = 0
for x in range(wholeRaceTime):
    if distTravelled(wholeRaceTime, x) > wholeDistRecord:
        spacer = x
        break
    
min_pbt = spacer
max_pbt = wholeRaceTime - spacer

P2 = max_pbt - min_pbt + 1

print("P2: ", P2)