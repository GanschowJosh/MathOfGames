"""
Designed to confirm validity of XKCD comic https://www.xkcd.com/3015/ 
"""
from itertools import product
from math import comb
def generate_outcome_table():
    d6 = [1, 2, 3, 4, 5, 6]
    d4 = [1, 2, 3, 4]
    outcome_table = {}

    for d6_rolls in product(d6, repeat=3):
        for d4_roll in d4:
            total = sum(d6_rolls) + d4_roll
            if total in outcome_table:
                outcome_table[total] += 1
            else:
                outcome_table[total] = 1

    return outcome_table



outcome_table = generate_outcome_table()
# for outcome, frequency in sorted(outcome_table.items()):
#     print(f"Outcome: {outcome}, Frequency: {frequency}")

# probability of rolling 16 or better amounts to the sum of the frequencies of the outcomes 16 through 22 divided by the sum of all frequencies
probability_16_or_higher = sum(outcome_table[x] for x in range(16, 23)) / sum(outcome_table.values())
print("Probability of rolling 16 or better: ", round(probability_16_or_higher, 4))

# probability of not grabbing any curseed arrows while grabbing 2 of the 10 arrows while 5 are cursed amounts to
# 5/10 * 4/9 because there are 5 cursed arrows and 4 non-cursed arrows left after grabbing the first arrow
probability_no_cursed_arrows = 5/10 * 4/9
print("Probability of not grabbing any cursed arrows while grabbing 2 of the 10 arrows while 5 are cursed: ", round(probability_no_cursed_arrows, 4))

# confirming the validity of the XKCD comic
print("Probabilities the same? ", "Yes:)" if probability_16_or_higher == probability_no_cursed_arrows else "No:(")
