# Sets

## Concept
A set is an unordered collection of unique elements (no duplicates).

---

## Key Operations

- **Union (A ∪ B)**  
  All elements from both sets  

- **Intersection (A ∩ B)**  
  Common elements between sets  

- **Difference (A - B)**  
  Elements in A but not in B  

---

## Python Application

Sets in Python are useful for:
- Removing duplicate elements  
- Fast membership checking (`in`)  
- Performing set operations efficiently  

---

## Example

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Union
print(a | b)   # {1, 2, 3, 4}

# Intersection
print(a & b)   # {2, 3}

# Difference
print(a - b)   # {1}

```

--- 

## Use in Computer Science

- Removing duplicates from datasets
- Database queries and filtering
- Search systems
- Recommendation systems

---

## Summary

- Sets are used to efficiently handle unique data and perform operations like union and intersection, which are fundamental in many computer science applications.