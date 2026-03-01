print('\n' + "-" * 154)
print('\n' + "NUMBER EVALUATOR".center(154))
print('\n' + "-" * 154)




while True:
    
    number = input("""

\n Enter P for Prime number
\n Enter A for Armstrong number
\n Enter L for LCM
\n Enter G for GCD
\n Enter Q to Quit 
\n > """).upper().strip()
    
    if( number == 'P'):
        
        n = int(input("Enter number: "))
        flag = True

        if n <= 1:
            flag = False
        elif n == 2:
            flag = True
        elif n % 2 == 0:
            flag = False
        else:
            i = 3
            while i  * i <= (n):
                if n % i == 0:
                    flag = False
                    break
                i += 2

        if flag:
                    print("\nPrime")
        else:
                    print("\nNot Prime")

    elif ( number == 'A'):
        n = int(input("Enter number: "))

        temp = n
        count = 0
        if temp == 0:
                count = 1
        while( temp > 0):
                
                count += 1
                temp //= 10
        
        temp = n
        total = 0
        while ( temp > 0):
                digit = temp % 10
                total += digit ** count
                temp //= 10

        if (total == n):
                print("\nArmstrong number")

        else:
            print("\nNot an Armstrong number")


    elif( number == 'G'):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            while( b != 0 ):
                  remainder = a % b
                  a = b
                  b = remainder

            print(f"\nGCD = {a}")

    elif( number == 'L'):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            
            x = a
            y = b
            while( b != 0 ):
                  remainder = a % b
                  a = b
                  b = remainder
            
            gcd = a
            lcm = (x * y) // gcd if gcd != 0 else 0
            print(f"\nLCM = {lcm}")

    elif( number == 'Q'):
          print("\nExiting the program...Bye")
          break
    
    else:
          print("\nEnter the evaluation correctly")

    

            

        
        
    
