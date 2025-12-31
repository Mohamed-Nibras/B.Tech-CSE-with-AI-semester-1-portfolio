name = input('Enter name: ')
if len(name) < 3:
    print('Name must be atleast 3 characters long ')

elif len(name) > 50:
    print('Name should not exceed 50 characters')

else:
    print('This name is fine ') 



    ask = int(input('Enter your weight: '))
    weight = input(" (L)bs or (K)g: ")


    if weight.upper() == "L":
        weight_lbs = ask * 0.45
        print(f"You are {weight_lbs} kilos ")

    elif weight.upper() == "K":
        weight_kg = ask / 0.45
        print(f"You are {weight_kg} pounds ")

