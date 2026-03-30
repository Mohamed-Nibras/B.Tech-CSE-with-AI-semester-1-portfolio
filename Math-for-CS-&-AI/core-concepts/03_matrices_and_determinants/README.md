# Matrices and Determinants

## Concept

A matrix is a rectangular array of numbers arranged in rows and columns.

A determinant is a scalar value calculated from a square matrix, used to determine properties like invertibility.

---

## Types of Matrices

- Row Matrix  
- Column Matrix  
- Square Matrix  
- Zero Matrix  
- Identity Matrix  
- Diagonal Matrix  

---

## Matrix Operations

- **Addition / Subtraction**  
  Performed element-wise  

- **Multiplication**  
  Possible only if:
  columns of A = rows of B  

- **Transpose**  
  Interchanging rows and columns  

---

## Determinant (Basic Idea)

- Defined only for square matrices  
- Helps determine:
  - whether a matrix is invertible  
  - properties of linear systems  

## Example (2×2 matrix):
| a b |
| c d |

Determinant = (a×d - b×c)


---

## Python Application

Matrices are represented using lists of lists.

---

## Example

```python
matrix = [[1, 2], [3, 4]]

total = 0
for row in matrix:
    for element in row:
        total += element

print(total)  # 10

```

---

## Use in Computer Science
- Computer graphics (2D/3D transformations)
- Machine learning (data representation, weights)
- Image processing (pixel grids)
- Solving systems of equations

---

## Summary

- Matrices are fundamental for representing structured data, while determinants help analyze matrix properties and solve mathematical systems used in computer science.