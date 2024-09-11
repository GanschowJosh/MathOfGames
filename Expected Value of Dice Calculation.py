inp = list(map(int, input("Enter number of sides: ").split()))

allTotal = 0
diceTotal = 0
running = 0
for item in inp:
    allTotal += sum(i for i in range(1, item+1))
    running += (allTotal / item)

print(f"EV: {running}")