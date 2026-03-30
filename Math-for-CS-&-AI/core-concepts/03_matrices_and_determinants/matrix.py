# Sample matrix

A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Accessing elements
print(A[0][1])  # Output: 2

# printing the entire matrix
for row in A:
    for element in row:
        print(element, end=' ')    
    print()  # for new line after each row

# Dimewnsions of the matrix
rows = len(A)
cols = len(A[0]) if rows > 0 else 0
print(f"Dimensions of the matrix: {rows} x {cols}")