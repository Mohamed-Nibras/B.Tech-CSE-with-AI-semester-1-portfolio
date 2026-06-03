name = input('Enter name: ')
price = 1000000


has_good = True
has_bad = False


if has_good:
    print(f"{name} , your final price is {0.1 * price} ")

elif has_bad:
    print(f"{name} , your final price is {0.2 * price} ")

else:
    print(f"{name} ,  your final price is {price} ")