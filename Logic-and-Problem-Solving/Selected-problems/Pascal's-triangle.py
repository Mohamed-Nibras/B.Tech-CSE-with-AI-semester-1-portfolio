# Pascal's triangle pattern

n = 5
for i in range(n):
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()


# Pascal Triangle (formula-based approach)
#
# Idea:
# - Each row starts with value = 1
# - Numbers are generated LEFT → RIGHT in the same row
# - Each next value is computed from the previous one
#
# Rule used:
#   next_value = current_value * (row_index - col_index) // (col_index + 1)
#
# Meaning (in simple words):
# - Move across the row without using previous rows
# - This formula safely generates the next Pascal number
#
# Note:
# - This is a math shortcut (binomial coefficient logic)
# - Useful to understand, NOT meant to be memorized
# - For learning dependency logic, list-based Pascal is clearer
#
# Mental hook:
# "Start with 1, keep updating value to get the next number in the row"

# Example for n = 5:
# Row 0: 1
# Row 1: 1 1    
# Row 2: 1 2 1  
# Row 3: 1 3 3 1
# Row 4: 1 4 6 4 1
# This code prints the first 5 rows of Pascal's triangle using the formula-based approach.
# Each row is built using the previous value in that row, without storing the entire triangle.
# This approach is efficient in terms of space and computation for generating Pascal's triangle.
# Example output for n = 5:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

