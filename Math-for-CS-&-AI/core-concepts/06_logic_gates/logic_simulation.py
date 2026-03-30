import shutil
width = shutil.get_terminal_size().columns
print("Logic Gate Simulator".center(width))

# AND gate
def AND_gate(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

# OR gate
def OR_gate(a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0
    
# NOT gate
def NOT_gate(a):
    if a == 1:
        return 0
    else:
        return 1
    
# NAND gate
def NAND_gate(a,b):
    return NOT_gate(AND_gate(a,b))

# NOR gate
def NOR_gate(a,b):
    return NOT_gate(OR_gate(a,b))

# XOR gate
def XOR_gate(a,b):
    return OR_gate(AND_gate(NOT_gate(a), b), AND_gate(a, NOT_gate(b)))

# Expression 1: (A AND B) OR (NOT C)
def expression1(a, b, c):
    expr1 = OR_gate(AND_gate(a, b), NOT_gate(c))
    return expr1

# Expression 2: A AND (B OR NOT C)
def expression2(a, b, c):
    expr2 = AND_gate(a, OR_gate(b, NOT_gate(c)))
    return expr2


while True:
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): ")) 
    c = int(input("Enter third input (0 or 1): "))

    if a not in [0, 1] or b not in [0, 1] or c not in [0, 1]:
        print("Invalid input. Please enter 0 or 1.")
        continue

    and_result = AND_gate(a, b)
    or_result = OR_gate(a, b)
    not_a = NOT_gate(a)
    nand_result = NAND_gate(a, b)
    nor_result = NOR_gate(a, b)
    xor_result = XOR_gate(a, b)
    expr1_result = expression1(a, b, c)
    expr2_result = expression2(a, b, c)
    print("GATE Results".center(width))
    print(f"AND({a}, {b}) = {and_result}")
    print(f"OR({a}, {b}) = {or_result}")
    print(f"NOT({a}) = {not_a}")
    print(f"NAND({a}, {b}) = {nand_result}")
    print(f"NOR({a}, {b}) = {nor_result}")
    print(f"XOR({a}, {b}) = {xor_result}")
    print("Expression Results".center(width))
    print(f"Expression 1 (A AND B) OR (NOT C) = {expr1_result}")
    print(f"Expression 2 A AND (B OR NOT C) = {expr2_result}")
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break
    else:
        print("\n")
