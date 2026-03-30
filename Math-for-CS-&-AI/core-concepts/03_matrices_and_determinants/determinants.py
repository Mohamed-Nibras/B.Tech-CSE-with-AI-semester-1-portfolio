# Determinants

def determinant(a, b, c, d):
    return a * d - b * c

# Example usage:
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
d = int(input("Enter value for d: "))
result = determinant(a, b, c, d)
print(f"The determinant of the matrix [[{a}, {b}], [{c}, {d}]] is: {result}")