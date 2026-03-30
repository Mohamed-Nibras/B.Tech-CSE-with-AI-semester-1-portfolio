print('\n' + '*' * 173)
print('\n' + 'MINI TRUTH TABLE GENERATOR'.center(173))
print('\n' + '*' * 173)

operator = input("Enter your operator(and, or, not): ").lower()

if operator == "and":
    A = [1,0]
    B = [1,0]
    
    print("\n|  A   |   B     |   A and B |")
    print("------------------------------")
     
    for x in A:
        for y in B:
            result = x and y
            print(f"|{x:^6}|{y:^9}|{result:^11}|")
            

elif operator == "or":
    A = [1,0]
    B = [1,0]
    
    print("\n|  A   |   B     |   A or B |")
    print("-----------------------------")
    for x in A:
        for y in B:
            result = x or y
            print(f"|{x:^6}|{y:^9}|{result:^10}|")
        

elif operator == "not":
    A = [1,0]
    B = [1,0]
    
    print("\n|  A   |   B     |   not A   |   not B     |")
    print("--------------------------------------------")
    for x in A:
        for y in B:
            result1 = not x
            result2 = not y
            print(f"|{x:^6}|{y:^9}|{result1:^11}|{result2:^13}|")

else:
    print("\nINVALID INPUT")
            

     