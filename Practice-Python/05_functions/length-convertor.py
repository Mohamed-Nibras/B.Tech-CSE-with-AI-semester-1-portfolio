
import shutil
width = shutil.get_terminal_size().columns # To analyze the terminal width
print("-" * width)
print(" Length Converter".center(width))
print("-" * width)

# Defining function
def meter_cm(meter):
    return meter * 100

def cm_meter(cm):
    return cm / 100

def km_meter(km):
    return km * 1000

def meter_km(meter):
    return meter / 1000

def feet_meter(feet):
    return feet * 0.3048

def meter_feet(meter):
    return meter / 0.3048

def inch_cm(inch):
    return inch * 2.54

def cm_inch(cm):
    return cm / 2.54

def mile_km(mile):
    return mile * 1.60934

def km_mile(km):
    return km / 1.60934


while True:

    length = (input("""\nChoose a conversion:

1) meter → cm
2) cm → meter
3) km → meter
4) meter → km
5) feet → meter
6) meter → feet
7) inch → cm
8) cm → inch
9) mile → km
10) km → mile
0) Exit

Enter choice: """)).strip()
    
    if not length.isdigit():
        print("\nEnter a number from 0 to 10.")
        continue
    length = int(length)
    
    if (length == 1):
        meter = float(input("Enter your length ( Meter to Centimeter): "))
        result1 = meter_cm(meter)
        print(f"\nResult = {result1} ")


    elif (length == 2):
        cm = float(input("Enter your length ( Centimeter to Meter ): "))
        result2 = cm_meter(cm)
        print(f"\nResult = {result2} ")


    elif (length == 3):
        km = float(input("Enter your length ( Kilometer to Meter ): "))
        result3 = km_meter(km)
        print(f"\nResult = {result3} ")


    elif (length == 4):
        meter = float(input("Enter your length ( Meter to Kilometer ): "))
        result4 = meter_km(meter)
        print(f"\nResult = {result4} ")


    elif (length == 5):
        feet = float(input("Enter your length ( Feet to Meter ): "))
        result5 = feet_meter(feet)
        print(f"\nResult = {result5} ")


    elif (length == 6):
        meter = float(input("Enter your length ( Meter to Feet ): "))
        result6 = meter_feet(meter)
        print(f"\nResult = {result6} ")


    elif (length == 7):
        inch = float(input("Enter your length ( Inch to Centimeter ): "))
        result7 = inch_cm(inch)
        print(f"\nResult = {result7} ")


    elif (length == 8):
        cm = float(input("Enter your length ( Centimeter to Inch ): "))
        result8 = cm_inch(cm)
        print(f"\nResult = {result8} ")


    elif (length == 9):
        mile = float(input("Enter your length ( Mile to Kilometer ): "))
        result9 = mile_km(mile)
        print(f"\nResult = {result9} ")


    elif (length == 10):
        km = float(input("Enter your length ( Kilometer to Mile ): "))
        result10 = km_mile(km)
        print(f"\nResult = {result10} ")


    elif (length == 0):
        print("\nExiting the program....Byee ✅")
        break


    else :
        print("\nEnter CONVERSION correctly( Example: 2 for cm → meter )")