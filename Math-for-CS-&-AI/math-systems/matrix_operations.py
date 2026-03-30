# Matrix addition and multiplication

# Matrix addition
def matrix_addition(matrix_a, matrix_b):
    # Check if the dimensions of the matrices are the same
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

# Matrix multiplication
def matrix_multiplication(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0

    if cols_a != rows_b:
        raise ValueError("Incompatible matrix dimensions")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

# Creating matrix
def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

# Example menu
def main():
    print("Matrix Operations")
    print("1. Matrix Addition")
    print("2. Matrix Multiplication")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        rows = int(input("Enter number of rows for the matrices: "))
        cols = int(input("Enter number of columns for the matrices: "))
        print("Enter values for Matrix A:")
        matrix_a = create_matrix(rows, cols)
        print("Enter values for Matrix B:")
        matrix_b = create_matrix(rows, cols)
        result = matrix_addition(matrix_a, matrix_b)
        print("Result of Matrix Addition:")
        for row in result:
            print(' '.join(map(str, row)))

    elif choice == '2':
        rows_a = int(input("Enter number of rows for Matrix A: "))
        cols_a = int(input("Enter number of columns for Matrix A: "))
        print("Enter values for Matrix A:")
        matrix_a = create_matrix(rows_a, cols_a)
        rows_b = int(input("Enter number of rows for Matrix B: "))
        cols_b = int(input("Enter number of columns for Matrix B: "))
        print("Enter values for Matrix B:")
        matrix_b = create_matrix(rows_b, cols_b)
        try:
            result = matrix_multiplication(matrix_a, matrix_b)
        except ValueError as e:
            print(e)
            return
        print("Result of Matrix Multiplication:")
        for row in result:
            print(" ".join(map(str, row)))

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()