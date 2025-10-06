#Title

print('\n' + "~" * 154)
print('\n' + "NUMBER BASE CONVERTOR".center(154) )
print('\n' + "~" * 154)

all_base = [ ]
all_numbers = [ ]
all_convertednumbers = [ ]
while True:
  convert = input("""\n
Enter BIN for Binary
Enter OCT for Octal
Enter HEX for Hexadecimal
Enter QUIT to quit this program

""").upper()

  if convert == "BIN":
              
      number = input("\nEnter your decimal number that you want to convert : ")

      while not number.isdigit():
         print("\nEnter valid number")
         number = input("\nEnter your decimal number that you want to convert : ")
      
      x = int(number)
      print(f"\nBinary:{bin(x)  [2:]}")
      base_name = "Binary"
      
      all_numbers.append(x)
      all_convertednumbers.append(bin(x) [2: ])
      all_base.append(base_name)


  elif convert == 'OCT':
      
      number = input("\nEnter your decimal number that you want to convert : ")

      while not number.isdigit():
         print("\nEnter valid number")
         number = input("\nEnter your decimal number that you want to convert : ")
      
      x = int(number)
      print(f"\nOctal:{oct(x)  [2:]}")
      base_name = "Octal"

      all_numbers.append(x)
      all_convertednumbers.append(oct(x) [2: ])
      all_base.append(base_name)

  elif convert == 'HEX':
      
      number = input("\nEnter your decimal number that you want to convert : ")

      while not number.isdigit():
         print("\nEnter valid number")
         number = input("\nEnter your decimal number that you want to convert : ")
      
      x = int(number)
      print(f"\nHexadecimal:{hex(x)  [2:].upper()}")
      base_name = "Hexadecimal"
      
      hex_num = hex(x)  [2:].upper()
      all_numbers.append(x)
      all_convertednumbers.append(hex_num)
      all_base.append(base_name)


  elif convert == 'QUIT':
      
      if all_convertednumbers != []:
          print('\n' + "~" * 154)
          print('\n' + "YOUR CONVERTED NUMBERS".center(154) )
          print('\n' + "~" * 154)
          for numbers, bases, converted in zip(all_numbers, all_base, all_convertednumbers):
                                        print(f"\nDecimal: {numbers}--->{bases}: {converted}") #ZIP() matches each elements with index 0 to 0, 1 to 1...
            
          print('\n' + "~" * 154)
          print('\n' + "THANKS FOR USING THIS PROGRAM 🫱🏻‍🫲🏻".center(154) )
          print('\n' + "~" * 154)
          break

      else :
          print('\n' + "~" * 154)
          print('\n' + "NO NUMBERS CONVERTED".center(154) )
          print('\n' + "~" * 154)
          print('\n' + "~" * 154)
          print('\n' + "THANKS FOR USING THIS PROGRAM 🫱🏻‍🫲🏻".center(154) )
          print('\n' + "~" * 154)
          break

  else :
      print("\nInvalid option ---> Enter BIN OCT HEX or QUIT ")

          
        
      
      

