"""
Carnival game with 7 red marbles (worth $-5),
                   5 green marbles (worth $3)
                   3 blue marbles (worth $6)

                   
Calculated: expected values from drawing 1..15 marbles from the bag
Simplified to fractions
"""

from itertools import combinations #every nCk combination
from math import comb #n choose k
from fractions import Fraction 

eachOutcome = 0
currCombs = []
outcomes = []

red = list(i for i in range(1, 8))
green = list(i for i in range(8, 13))
blue = list(i for i in range(13, 16))

Range = range(1, 16)

for i in range(1, 16):
    currMax = comb(15, i) #nCk
    val = 0 #total value from drawing from bag of each combination
    currCombs = combinations(Range, i)
    for com in currCombs:
        for item in com:
            if item in red:
                val -= 5
            elif item in green:
                val += 3
            elif item in blue:
                val += 6
    outcomes.append(Fraction(val/currMax).limit_denominator())

print(list(f"{int(Fraction(outcome).numerator)}/{int(Fraction(outcome).denominator)}" for outcome in outcomes))

