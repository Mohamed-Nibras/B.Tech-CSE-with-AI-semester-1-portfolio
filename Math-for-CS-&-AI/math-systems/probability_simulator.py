import random

def simulate_dice():
    n = 1000
    count_7 = 0
    count_2 = 0

    for i in range(n):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        total = dice1 + dice2

        if total == 7:
            count_7 += 1
        if total == 2:
            count_2 += 1

    print("\n--- Dice Simulation ---")
    print("P(sum = 7) ≈", count_7 / n)
    print("P(sum = 2) ≈", count_2 / n)


def simulate_coins():
    n = 1000
    count_exact = 0
    count_atleast = 0

    for i in range(n):
        toss1 = random.choice(["H", "T"])
        toss2 = random.choice(["H", "T"])

        if (toss1 == "H" and toss2 == "T") or (toss1 == "T" and toss2 == "H"):
            count_exact += 1

        if toss1 == "H" or toss2 == "H":
            count_atleast += 1

    print("\n--- Coin Simulation ---")
    print("P(exactly one head) ≈", count_exact / n)
    print("P(at least one head) ≈", count_atleast / n)


simulate_coins()
simulate_dice()