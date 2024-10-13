

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

from collections import defaultdict
def seventhInningStretch():
    coloradoPoss = [(i, j) for i in range(1, 7) for j in range(1, 7)] #roll 2, score runs equal to min value minus one
    
    coloradoEV = 0
    coloradoDict = defaultdict(list)
    for i, j in coloradoPoss:
        coloradoDict[min(i, j)-1].append((i,j))
    for k, v in coloradoDict.items():
        #print(f"{k}: {len(v)}")
        coloradoEV += k*len(v)
    
    #print(coloradoEV/36)

    coloradoPoss2 = [i for i in range(1, 7)]
    coloradoEV2 = 0
    coloradoDict2 = defaultdict(list)
    for i in coloradoPoss2:
        coloradoDict2[i-1].append(i)
    for k, v in coloradoDict2.items():
        #print(f"{k}: {len(v)}, {v}")
        coloradoEV2 += k*len(v)
    
    #print(coloradoEV2/6)
    

    floridaPoss = [(i,j,k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)] #roll 3, score 0 runs if the sum is less than 9, else 2 runs

    floridaEV = 0
    floridaDict = defaultdict(list)
    for i, j, k in floridaPoss:
        if i+j+k < 9:
            floridaDict[0].append((i, j, k))
        else:
            floridaDict[2].append((i, j, k))
    for k, v in floridaDict.items():
        #print(f"{k}: {len(v)}")
        floridaEV += k*len(v)
    
    #print(floridaEV/(36*6))

    floridaPoss2 = [(i, j, k, l) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7) for l in range(1, 7)]
    floridaEV2 = 0
    floridaDict2 = defaultdict(list)
    for i, j, k, l in floridaPoss2:
        if i+j+k+l < 9:
            floridaDict2[0].append((i, j, k, l))
        else:
            floridaDict2[2].append((i, j, k, l))
    for k, v in floridaDict2.items():
        #print(f"{k}: {len(v)}, {v[:4]}")
        floridaEV2 += k*len(v)
    #print(floridaEV2/(6**4))

    clevelandPoss = [(i,j) for i in range(1, 7) for j in range(1, 7)] #roll 2, score one run for every four pips showing
    clevelandDict = defaultdict(list)
    clevelandEV = 0
    for i, j in clevelandPoss:
        clevelandDict[(i+j)//4].append((i, j))
    for k, v in clevelandDict.items():
        #print(f"{k}: {len(v)}")
        clevelandEV += k*len(v)
    #print(clevelandEV/36)

    clevelandPoss2 = [(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)]
    clevelandDict2 = defaultdict(list)
    clevelandEV2 = 0
    for i, j, k in clevelandPoss2:
        clevelandDict2[(i+j+k)//4].append((i, j, k))
    for k, v in clevelandDict2.items():
        clevelandEV2+=k*len(v)
        #print(f"{k}: {len(v)}, {v[:4]}")
    #print(clevelandEV2/216)

    seattlePoss = []
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                seattlePoss.append((i, j, k)) #roll 3, score runs equal to the difference between the two lowest dice
    seattleDict = defaultdict(list)
    seattleEV = 0
    for i, j, k in seattlePoss:
        seattleDict[sorted([i, j, k])[1] - sorted([i, j, k])[0]].append((i, j, k))
    
    for k, v in seattleDict.items():
        #print(f"{k}: {len(v)}, {v[:4]}")
        seattleEV += k*len(v)
    #print(seattleEV/(216))

    seattlePoss2 = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    seattleDict2 = defaultdict(list)
    seattleEV2 = 0
    for i, j in seattlePoss2:
        seattleDict2[abs(i-j)].append((i, j))
    for k, v in seattleDict2.items():
        seattleEV2 += k*len(v)
        #print(f"{k}: {len(v)}, {v[:4]}")
    #print(seattleEV2/36)


    minnesotaPoss = [i for i in range(1, 7)] #roll 1, score runs equal to the distance of the value from 4
    minnesotaDict = defaultdict(list)
    minnesotaEV = 0
    for i in minnesotaPoss:
        minnesotaDict[abs(i-4)].append(i)
    for k, v in minnesotaDict.items():
        #print(f"{k}: {len(v)}, {v}")
        minnesotaEV += k*len(v)
    #print(minnesotaEV/6)

    minnesotaPoss2 = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    minnesotaDict2 = defaultdict(list)
    minnesotaEV2 = 0
    for i, j in minnesotaPoss2:
        minnesotaDict2[abs((i+j)-4)].append((i, j))
    for k, v in minnesotaDict2.items():
        minnesotaEV2 += k*len(v)
        print(f"{k}: {len(v)}, {v[:4]}")
    print(minnesotaEV2/36)
seventhInningStretch()