# Calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
def permutations(n, r):
    if r > n:
        return 0
    else:
        return factorial(n) // factorial(n - r)

def combinations(n, r):
    if r > n:
        return 0
    else:
        return factorial(n) // (factorial(r) * factorial(n - r))
    
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
# Calculate permutations
permutation = permutations(n, r)
print(f"Permutations of {n} items taken {r} at a time: {permutation}")
# Calculate combinations
combination = combinations(n, r)
print(f"Combinations of {n} items taken {r} at a time: {combination}")