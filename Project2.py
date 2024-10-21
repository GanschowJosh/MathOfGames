"""
The game General Orders: World War II includes four custom dice that have the following six faces: 0, 1, 1, 1, 1, 2.
To resolve combat according to the original rules, the defender rolls one die and removes the resulting number of troops from the attackers unit,
then both players remove troops one at a time until one or both players run out of troops. This system results in battles where the outcome is predetermined
(e.g. attacker has 6 troops, defender has three) and where ties are possible. Your job is to determine a better system for resolving combat, using only
the four custom dice that come with the game.
"""

from itertools import product #returns cartesian product of a given set, useful for generation of outcomes for an arbitrary number of dice
from collections import defaultdict

die = [0, 1, 1, 1, 1, 2]

"""
Testing outcomes with attacker starting with 6 and defender starting with 4, showing guaranteed outcome of win for attacker
"""
def initialCase():
    cases = []
    for i in range(len(die)):
        for j in range(len(die)):
            cases.append((die[i], die[j]))
    
    outcomes = defaultdict(list)

    for a, b in cases:
        attacker = 6 - a
        defender = 3 - b

        if attacker > defender: #attacker wins with this roll combo
            outcomes["attacker"].append((a, b))
        elif defender > attacker: #defender wins with this roll combo
            outcomes["defender"].append((a, b))
        else: #tie with this roll combo
            outcomes["tie"].append((a, b))

    for k, v in outcomes.items():
        print(f"{k}: {len(v)}, {v[:3]}")


"""
Testing outcomes where the only the one with the advantage of numbers rolls, and the number being rolled is determined by how advantaged they are
Verdict: not a better system
"""
def testCase1(attacker, defender): #attacker starting score and defender starting score
    if attacker > defender:
        numRolled = attacker-defender
    else:
        numRolled = defender-attacker
    
    tempAttacker = attacker
    tempDefender = defender

    rolls = list(product(die, repeat=numRolled))

    rolls = map(list, (item for item in rolls))
    outcomes = defaultdict(list) #storing all the outcomes

    for item in rolls:
        tempAttacker = attacker
        tempDefender = defender
        if attacker > defender: #attacker is advantaged
            tempAttacker -= sum(item)
        else: #defender is advantaged
            tempDefender -= sum(item)
        
        if tempAttacker > tempDefender: #attacker wins this roll
            outcomes["attacker"].append(item)
        elif tempDefender > tempAttacker:
            outcomes["defender"].append(item)
        else:
            outcomes["tie"].append(item)
        
    for k, v in outcomes.items():
        print(f"{k}: {len(v)}, {v[:4]}")

def testCase2(attacker, defender):
    outcomes = defaultdict(list)

    # Rolls for attacker and defender based on their troop counts
    attacker_rolls = list(product(die, repeat=attacker))
    defender_rolls = list(product(die, repeat=defender))

    attacker_rolls = map(list, (item for item in attacker_rolls))
    defender_rolls = map(list, (item for item in defender_rolls))

    for a_roll in attacker_rolls:
        for d_roll in defender_rolls:
            # Calculate the sum of dice rolls
            attacker_sum = sum(a_roll)
            defender_sum = sum(d_roll)

            # Multiply sum by troop count to get effective result
            attacker_effective = attacker_sum * attacker
            defender_effective = defender_sum * defender

            # Determine final outcome (no ties or partial victories)
            if attacker_effective > defender_effective:
                # Attacker wins, defender loses all troops
                outcomes["attacker"].append((a_roll, d_roll))
            else:
                # Defender wins, attacker loses all troops
                outcomes["defender"].append((a_roll, d_roll))

    # Output results for analysis
    for k, v in outcomes.items():
        print(f"{k}: {len(v)}, {v[:4]}")  # Showing first 4 outcomes for each result

def testCase3():
    def printOutcomes(outcomes): #prints the outcomes
        total = sum(outcomes.values()) #calculates the total number of outcomes
        print(f"Total possible outcomes: {total}")
        print("\nDetailed outcomes:")
        #sorts outcomes by occurrences, then attacker and defender troop counts
        for (a, d), count in sorted(outcomes.items(), key=lambda x: (-x[1], -x[0][0], -x[0][1])):
            if a > 0 and d == 0:
                result = "Attacker wins"
            elif a == 0 and d > 0:
                result = "Defender wins"
            else:
                continue  # Skip any remaining ties
            print(f"{result} - Attacker: {a}, Defender: {d} - Occurrences: {count}")
    
    def analyzeOutcomes(outcomes):
            total = sum(outcomes.values())
            probabilities = {k: v / total for k, v in outcomes.items()}
            attacker_wins = sum(count for (a, d), count in outcomes.items() if a > 0 and d == 0)
            defender_wins = sum(count for (a, d), count in outcomes.items() if d > 0 or (a == 0 and d == 0))

            expected_attacker_troops = sum(a*(count/total) for (a, d), count in outcomes.items())
            expected_defender_troops = sum(d*(count/total) for (a, d), count in outcomes.items())

            print(f"Probability of Attacker winning: {attacker_wins / total:.2%}")
            print(f"Probability of Defender winning: {defender_wins / total:.2%}")
            print(f"Expected remaining Attacker troops: {expected_attacker_troops:.2f}")
            print(f"Expected remaining Defender troops: {expected_defender_troops:.2f}")
            print("\nProbability distribution:")
            for (a, d), prob in sorted(probabilities.items(), key=lambda x: (-x[1], -x[0][0], -x[0][1])):
                print(f"Attacker: {a}, Defender: {d} - Probability: {prob:.2%}")

            print()
            printOutcomes(outcomes)

    #simualtes combat between attacker and defender
    def simulateCombat(attacker, defender):
        die = [0, 1, 1, 1, 1, 2] #custom die

        #function determines the number of dice to roll based on the number of troops the party has left
        def rollDice(troops):
            if troops <= 2:
                return 1
            elif troops <= 4:
                return 2
            elif troops <= 6:
                return 3
            else:
                return 4
        
        #simulates a single round given the number of troops for each party
        def simulateRound(a_troops, d_troops):
            a_dice = rollDice(a_troops)
            d_dice = rollDice(d_troops)

            outcomes = defaultdict(int)
            
            #simulates all possible dice rolls for attacker and defender
            for a_roll in product(die, repeat=a_dice):
                for d_roll in product(die, repeat=d_dice):
                    a_sum = sum(a_roll)
                    d_sum = sum(d_roll)

                    if a_sum > d_sum: #attacker wins the round
                        new_d_troops = max(0, d_troops - (a_sum - d_sum))
                        outcomes[(a_troops, new_d_troops)] += 1
                    elif d_sum > a_sum: #defender wins the round
                        new_a_troops = max(0, a_troops - (d_sum - a_sum))
                        outcomes[(new_a_troops, d_troops)] += 1
                    else:
                        # In case of a tie, both lose 1 troop
                        outcomes[(max(0, a_troops - 1), max(0, d_troops - 1))] += 1
            
            return outcomes #returns all the outcomes for the given round

        results = {(attacker, defender): 1} #initial result, start with given attacker and defender troop counts
        
        while True:
            new_results = defaultdict(int)
            for (a, d), count in results.items():
                if a == 0 or d == 0:
                    new_results[(a, d)] += count #if any side is out of troops, no more rounds
                else:
                    round_outcomes = simulateRound(a, d) #simulates the round
                    for outcome, outcome_count in round_outcomes.items():
                        new_results[outcome] += count * outcome_count #udpates the outcomes based on the simulated round
            
            if new_results == results:
                break #stop if there are no new outcomes generated, (i.e., the simulation stabilizes)
            results = new_results #updates results for the next round
        
        return results

    initialAttacker = 5 #initial number of attacker troops
    initialDefender = 3 #initial number of defender troops

    print(f"Initial state: {initialAttacker}, {initialDefender}")
    results = simulateCombat(initialAttacker, initialDefender) #runs the simulation
    analyzeOutcomes(results) #analyzes and prints the outcomes

    
testCase3()