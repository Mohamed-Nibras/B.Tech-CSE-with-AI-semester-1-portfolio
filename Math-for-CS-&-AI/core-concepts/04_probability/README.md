# Probability

## Concept
Probability measures how likely an event is to occur, ranging from 0 to 1.

---

## Formula

P(E) = Number of favorable outcomes / Total number of possible outcomes

---

## Key Concepts

- **Independent Events**  
  One event does not affect another  

- **Dependent Events**  
  One event affects another  

---

## Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even = [n for n in numbers if n % 2 == 0]

probability = len(even) / len(numbers)
print(probability)  # 0.5

```

---

## Use in Computer Science

- Machine learning predictions
- Spam detection systems
- Recommendation systems
- Risk analysis

---

## Summary

- Probability is essential for making predictions and decisions under uncertainty, and it plays a key role in artificial intelligence and data-driven systems.