import random

while True:
    que1 = str(input("Generate a new number?\n")).lower()
    if que1 == "yes":
        varX = [0.312, 0.432, 0.244, 0.247, 0.7687, 0.235, 0.23945, 0.93458, 0.34806, 0.495]
        varR = [13, 3, 6, 3, 8, 17, 2984756]
        var1 = 1 - random.choice(varX)
        var2 = random.choice(varR) * random.choice(varX)
        randomnum = var1 * var2
        print(randomnum)
    else:
        print("You dumb stupid titty knuckle bringle bum tooth man")
