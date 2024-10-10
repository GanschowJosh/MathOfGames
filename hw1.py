from collections import defaultdict
def experimentA():
    table = defaultdict(list)
    for r in range(1, 7):
        for g in range(1, 7):
            table[min(0, r-g)].append((r, g))

    totalPoss = 36
    ev = 0

    for k, v in table.items():
        print(f"{k}: {len(v)}")
        curr = k*(len(v))
        ev += curr

    print(f"x_i*|x_i| total: {ev}")
    print(f"EV: {ev/totalPoss}")


from math import comb
from itertools import combinations
def experimentB():
    deck = [_%13 for _ in range(52)]
    score = {0: 100,
             12: 60,
             11: 30,
             10: 10,
             1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5}
    rep = {0: 'A',
           12: 'K',
           11: 'Q',
           10: 'J',
           1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
    combin = combinations(deck, 2) #all 2-card combinations
    allScores = defaultdict(list)
    total = 0
    for c in combin: #looping through all combinations
        currScore = score[c[0]] + score[c[1]] #adding score of two cards
        allScores[currScore].append((c[0], c[1]))
        total += 1

    ev = 0
    for k,v in sorted(allScores.items()):
        print(f"{k}: {len(v)}, {k*len(v)}")
        ev += k*len(v)
        """for a, b in v[:3]:
            print(f"{rep[a]},{rep[b]}", end="||")
        print(ev)"""
    print(ev)
    ev/=total
    print(ev)

def experimentC():
    #defining dice (3 red, 2 blue, 1 green)
    #each tuple represents a die with (color, value)
    colors = ['red', 'red', 'red', 'green', 'green', 'blue']
    dice = []
    print(dice)
    payouts = defaultdict(list)
    #rolls = combinations(dice, 2) #all possible combinations of two rolls
    
    """for roll in rolls:
        a, b = roll
        if a[0] == b[0] and a[1] == b[1]: #both color and roll match
            payouts[10].append((a, b))
        elif a[0] == b[0] or a[1] == b[1]: #either color or roll match
            payouts[4].append((a, b))
        else: #none match
            payouts[-3].append((a, b))
    
    for k, v in payouts.items():
        print(f"{k}: {len(v)}")
        print(v[:3])"""



experimentC()