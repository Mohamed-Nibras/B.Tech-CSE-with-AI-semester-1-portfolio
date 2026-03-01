# Fibonacci sequence using recursion

def fibonacci(n):
    
    # BASE CASE:
    # If n is 0 → return 0
    # If n is 1 → return 1
    # These are the starting values of Fibonacci sequence
    if n <= 1:
        return n
    
    # RECURSIVE CASE:
    # fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    # This creates TWO recursive calls (branching)
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example:
# fibonacci(5)
# = fib(4) + fib(3)
#
# fib(4)
# = fib(3) + fib(2)
#
# fib(3)
# = fib(2) + fib(1)
#
# fib(2)
# = fib(1) + fib(0)
#
# Base cases:
# fib(1) = 1
# fib(0) = 0
#
# Now values return:
# fib(2) = 1 + 0 = 1
# fib(3) = 1 + 1 = 2
# fib(4) = 2 + 1 = 3
# fib(5) = 3 + 2 = 5

n = int(input("Enter a number: "))
print(fibonacci(n))
