import random

count_atleast = 0
count_exact = 0
n = 1000

for i in range(n):
    toss1 = random.choice(["H", "T"])
    toss2 = random.choice(["H", "T"])

    # exactly one head
    if (toss1 == "H" and toss2 == "T") or (toss1 == "T" and toss2 == "H"):
        count_exact += 1

    # at least one head
    if toss1 == "H" or toss2 == "H":
        count_atleast += 1

print("P(exactly one head) ≈", count_exact/n)
print("P(at least one head) ≈", count_atleast/n)