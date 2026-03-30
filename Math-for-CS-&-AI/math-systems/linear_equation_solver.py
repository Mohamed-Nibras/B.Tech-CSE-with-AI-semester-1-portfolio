import numpy as np

equation = int(input("Enter number of equations: "))
n = int(input("Enter number of variables: "))

if equation != n:
    print("Number of equations must be equal to number of variables for a unique solution.")
    exit()

A = []

print("\nEnter coefficients of the variables in each equation:")
for i in range(equation):
    print(f"\nCo-efficents of {n} variables in equation {i+1}: \n", end="")
    row = list(map(float, input(f"Equation {i+1}: ").split()))
    A.append(row)

print("\nEnter constants of the equations:")
B = list(map(float, input().split()))

A = np.array(A)
B = np.array(B)

for i in range(equation):
    print(f"Equation {i+1}: ", end="")
    print(A[i], "=", B[i])
try:
    X = np.linalg.solve(A, B)
    print("Solution:", X)

except np.linalg.LinAlgError:
    print("No unique solution")