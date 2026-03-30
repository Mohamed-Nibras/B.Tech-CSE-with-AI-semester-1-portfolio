import shutil
width = shutil.get_terminal_size().columns


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:        
        return n * factorial(n - 1)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def nPr(n, r):
    if r == 0:
        return 1
    elif r > n or n < 0 or r < 0:
        raise ValueError("Invalid input. Ensure that n >= r >= 0.")
    else:
        return factorial(n) // factorial(n - r)  

def nCr(n, r):
    if r == 0 or r == n:
        return 1
    elif r > n or n < 0 or r < 0:
        raise ValueError("Invalid input. Ensure that n >= r >= 0.")
    else:
        return factorial(n) // (factorial(r) * factorial(n - r))

def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
while True:
    print("\n" + "=" * width)
    print("Math Toolkit".center(width))
    print("=" * width)
    print("1. Factorial")
    print("2. GCD")
    print("3. LCM")
    print("4. nPr")
    print("5. nCr")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        num = get_input("Enter a number: ")
        try:
            print(factorial(num))
        except ValueError as e:
            print(e)

    elif choice == "2":
        a = get_input("Enter first number: ")
        b = get_input("Enter second number: ")
        print("GCD:", gcd(a, b))

    elif choice == "3":
        a = get_input("Enter first number: ")
        b = get_input("Enter second number: ")
        print("LCM:", lcm(a, b))

    elif choice == "4":
        n = get_input("Enter n: ")
        r = get_input("Enter r: ")
        try:
            print("nPr:", nPr(n, r))
        except ValueError as e:
            print(e)

    elif choice == "5":
        n = get_input("Enter n: ")
        r = get_input("Enter r: ")
        try:
            print("nCr:", nCr(n, r))
        except ValueError as e:
            print(e)

    elif choice == "6":        
        print("Exiting...")
        break   
    
    else:        
        print("Invalid choice")
                