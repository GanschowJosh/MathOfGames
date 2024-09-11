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

currCombs = []                          #list for storing all the current combinations from a given k val
outcomes = []                           #list for storing all the outcomes to be printed at the end

red = list(_ for _ in range(1, 8))      #numbering off all red dice (7 of them)
green = list(_ for _ in range(8, 13))   #numbering off all green dice (5 of them)
blue = list(_ for _ in range(13, 16))   #numbering off all blue dice (3 of them)

Range = range(1, 16)

for k in range(1, 16): #lowest..highest+1 number of marbles pulled out each time
    currMax = comb(15, k) #nCk for current k
    val = 0 #total value from drawing from bag of each combination
    currCombs = combinations(Range, k)
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

