
---

# 📁 `permutation-combination/README.md`

```markdown
# Permutations and Combinations

## Concept

Permutations and combinations are used to count the number of ways to arrange or select items.

- **Permutation** → arrangement matters  
- **Combination** → arrangement does not matter  

---

## Formulas

- **Permutation (nPr)**  
  nPr = n! / (n - r)!

- **Combination (nCr)**  
  nCr = n! / (r! × (n - r)!)

---

## Example

- Selecting 2 students out of 3:
  - Combination → order doesn’t matter  
- Arranging 2 students out of 3:
  - Permutation → order matters  

---

## Python Application

```python
import math

n = 5
r = 2

perm = math.factorial(n) // math.factorial(n - r)
comb = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

print(perm, comb)

```

---

## Use in Computer Science

- Probability calculations
- Algorithm design
- Optimization problems
- Cryptography

----

## Summary

- Permutations and combinations help solve counting problems and are essential in probability and algorithm design.