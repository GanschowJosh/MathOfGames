

def spots():
    dicePos = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    bad = 0 #number of busting outcomes counter
    ev = 0 #keep track of expected value
    placed1 = 0
    placed1list = []
    placed2 = 0
    placed2list = []

    for a, b in dicePos:
        openSpots = [1, 3, 4, 6]
        doghouse = 4
        placed = 0
        if a not in openSpots:
            doghouse += a
        else:
            openSpots = openSpots[:openSpots.index(a)] + openSpots[openSpots.index(a)+1:]
            ev += 1
            placed += 1
        if b not in openSpots:
            doghouse += b
        else:
            ev += 1
            placed += 1
        
        if doghouse > 7:
            bad += 1
            ev -= 1
        if placed == 1:
            placed1 += 1
            placed1list.append((a, b))
        elif placed == 2:
            placed2 += 1
            placed2list.append((a, b))
    print(bad)
    print(f"Placed 1: {placed1}, {placed1list}\n, Placed 2: {placed2}, {placed2list}\n, EV: {ev/36}")

def spotsWithReroll():
    dicePos = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    
    totalOutcomes = len(dicePos)

    bustCount = 0

    for a, b in dicePos:
        doghouse = 4
        openSpots = [1, 3, 4, 6]

        if a not in openSpots:
            doghouse += a
        else:
            openSpots.remove(a)
        
        if b not in openSpots:
            doghouse += b
        
        if doghouse > 7:

            for reroll in dicePos:
                a_reroll, b_reroll = reroll
                doghouse = 4
                openSpots = [1, 3, 4, 6]

                if a_reroll not in openSpots:
                    doghouse += a_reroll
                else:
                    openSpots.remove(a_reroll)
                
                if b_reroll not in openSpots:
                    doghouse += b_reroll

                if doghouse > 7:
                    bustCount += 1

    bustProb = bustCount / totalOutcomes**2
    print(bustProb)

def seventhInningStretch():
    coloradoPoss = [(min(i, j)-1) for i in range(1, 7) for j in range(1, 7)] #roll 2, score runs equal to min value minus one

    floridaPoss = [0 if i+j+k<9 else 2 for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)] #roll 3, score 0 runs if the sum is less than 9, else 2 runs

    clevelandPoss = [(i+j)//4 for i in range(1, 7) for j in range(1, 7)] #roll 2, score one run for every four pips showing

    seattlePoss = []
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                seattlePoss.append(sorted(i, j, k)[1]-sorted(i, j, k)[0]) #roll 3, score runs equal to the difference between the two lowest dice

    minnesotaPoss = [abs(i-4) for i in range(1, 7)] #roll 1, score runs equal to the distance of the value from 4