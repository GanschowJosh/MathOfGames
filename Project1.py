"""
You have access to an unlimited number of polyhedral dice (d4, d6, d8, d10, d12, d20).
Using at least two different types of dice, design a "game" that has possible values
ranging from 0 to at least 0 and an expected value very close to 5

My solution: take 2d20, 1d12, and 1d8 and roll them. Take smallest roll from those 4 (call it n)
and sum up all values below (not inlcuding n). The sum is your score. 
"""

#dice

from collections import defaultdict, OrderedDict

dice = [12, 8]
possibleSums = defaultdict(list)
total = 0
ev = 0
srt = []


"""for i in range(1, dice[0]+1):
    for j in range(1, dice[1]+1):
        for k in range(1, dice[2]+1):
            for l in range(1, dice[3]+1):
                srt = sorted([i, j, k, l]) #sorting values
                sum1 = sum(i for i in range(srt[0])) #summing all values below lowest rolled
                possibleSums[sum1].append((i, j, k, l))
                total += 1"""
            
for i in range(1, dice[0]+1):
    for j in range(1, dice[1]+1):
        #sum1 = sum(i for i in range(min(i, j)))
        sum2 = sum(i for i in range(min(i, j)))
        possibleSums[abs(sum2-max(i,j))].append((i, j))
        total+=1

od = OrderedDict(sorted(possibleSums.items()))
for k, v in od.items():
    curr = k*(len(v))
    print(f"{k}: {len(v)}")
    ev += curr
    print(curr)


print(f"total: {ev}")
print(f"expected value: {ev/total}")