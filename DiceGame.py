import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
sum = dice1 + dice2

print("Rolling the dice...")
print("Die 1: " + str(dice1))
print("Die 2: " + str(dice2))
print("Total value: " + str(sum))