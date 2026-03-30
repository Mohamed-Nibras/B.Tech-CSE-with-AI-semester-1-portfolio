import random

n = 1000
count_7 = 0
count_2 = 0

for i in range(n):
    # roll two dice
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    # check if sum == 7
    if dice1 + dice2 == 7:
        count_7 += 1
    if dice1 + dice2 == 2:
        count_2 += 1

print("P(sum = 7) ≈", count_7 / n)
print("P(sum = 2) ≈", count_2 / n)