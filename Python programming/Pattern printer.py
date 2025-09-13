print('\n' + "=" * 173 )
print('\n' + 'PATTERN PRINTER'.center(173))
print('\n' + "=" * 173 )

 
all_patterns = [ ]


while True:
 pattern = input('\n ' \
 '\nChoose the pattern you want to print: '
 '\n"R" for rectangle '
 '\n"T" for triangle '
 '\n"I" for inverse traingle '
 '\n"S" for square '
 '\n"Q" to Quit '
 '\n> ').upper()



 if  pattern == "R":
        word = input("Enter the word you want to print: ")
        rows = input("Enter number of rows: ")
        column = input("Enter number of columns: ")
        while not (rows.isdigit() and column.isdigit()):
            print("Row and Column should be numbers!")
            rows = input("Enter number of rows: ")
            column = input("Enter number of columns: ")
        rows = int(rows)
        column = int(column)
        pattern_str = ""
        for i in range(rows):
         for o in range(column):
          pattern_str += word + " "
         pattern_str += "\n"
         
        print(pattern_str)
        all_patterns.append("Rectangle:\n" + pattern_str)
    
  
 elif pattern == "T":
        word = input("Enter the word you want to print: ")
        rows = input("Enter number of rows: ")
        while not rows.isdigit(): 
            print("Row and Column should be numbers!")
            rows = input("Enter number of rows: ")
        rows = int(rows)
        pattern_str = ""
        for t in range(1, rows+1):
         space = " " * (rows - t)
         pattern_str +=  space + (word + " ")* t
         pattern_str += "\n"
        print(pattern_str)
        all_patterns.append("Triangle:\n" + pattern_str)
    
  
 elif pattern == "I":
        word = input("Enter the word you want to print: ")
        rows = input("Enter number of rows: ")        
        while not rows.isdigit() :
            print("Row and Column should be numbers!")
            rows = input("Enter number of rows: ")
        rows = int(rows)
        pattern_str = ""
        for t in range(rows , 0 , -1):
         space = " " * (rows - t)
         pattern_str += space + (word + " ")* t
         pattern_str += "\n"
        print(pattern_str)
        all_patterns.append("Inverse Triangle:\n" + pattern_str)
    
    
  
 elif pattern == "S":
        word = input("Enter the word you want to print: ")
        while True:
            rows = input("Enter number of rows: ")
            column = input("Enter number of columns: ")
            if rows.isdigit() and column.isdigit():
                rows = int(rows)
                column = int(column)
                if rows == column:
                    pattern_str = ""
                    for p in range(rows):
                        for y in range(column):
                            pattern_str += word + " "
                        pattern_str += "\n"
                    print(pattern_str)
                    all_patterns.append("Square:\n" + pattern_str)
                    break
                else:
                    print("For a square, rows and columns must be equal!")
            else:
                print("Rows and Columns must be numbers!")
    
    
 elif pattern == 'Q':
   if  all_patterns != []:
    print('\n' + "-" * 173 )
    print('\n' + 'ALL PATTERNS PRINTED'.center(173))
    print('\n' + "-" * 173 )
    for stored in all_patterns:
       print(stored)
    print('\n' + "=" * 173 )
    print('\n' + 'EXITING....BYEEE 👋👋👋'.center(173))
    print('\n' + "=" * 173 )
    break 
   else :
       print('\n' + "-" * 173 )
       print('\n' + 'NO PATTERNS PRINTED'.center(173))
       print('\n' + "-" * 173 )
       print('\n' + "=" * 173 )
       print('\n' + 'EXITING....BYEEE 👋👋👋'.center(173))
       print('\n' + "=" * 173 )
       break 
 else: 
    print('Enter Pattern correctly')
   
    