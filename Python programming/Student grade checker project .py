name = input('Enter your full name: ')
if len(name) < 3 or len(name) > 50:
    print('Name must be between 3 to 50 characters ')

print(f"Hi , {name} ")
    
grade = int(input('Enter your grade: '))

if grade <= 10 :
    eng = int(input('Enter English mark: '))
    lan = int(input('Enter Second Language mark: '))
    mat = int(input('Enter Mathematics mark: '))
    sci = int(input('Enter Science mark: '))
    soc = int(input('Enter Social Science mark: '))


    if eng >=91 or eng == 100 :
     print("English: A1 ")

    elif eng >= 81 or eng == 90 :
     print("English: A2 ")

    elif eng >= 71 or eng == 80 :
     print("English: B1 ")

    elif eng >= 61 or eng == 70 :
     print("English: B2 ")

    elif eng >= 51 or eng == 60 :
     print("English: C1 ")

    elif eng >= 41 or eng == 50 :
     print("English: C2 ")

    elif eng >= 35 or eng == 40 :
     print("English: D ") 

    else :
     print('English: Fail , needs improvement ')

    
    if lan >=91 or lan == 100 :
     print("Second language: A1 ")

    elif lan >= 81 or lan == 90 :
     print("Second language: A2 ")

    elif lan >= 71 or lan == 80 :
     print("Second language: B1 ")

    elif lan >= 61 or lan == 70 :
     print("Second language: B2 ")

    elif lan >= 51 or lan == 60 :
     print("Second language: C1 ")

    elif lan >= 41 or lan == 50 :
     print("Second language: C2 ")

    elif lan >= 35 or lan == 40 :
     print("Second language: D ") 

    else :
     print('Second language: Fail , needs improvement ') 
 


    if mat >=91 or mat == 100 :
     print("Mathematics: A1 ")

    elif mat >= 81 or mat == 90 :
     print("Mathematics A2 ")

    elif mat >= 71 or mat == 80 :
     print("Mathematics: B1 ")

    elif mat >= 61 or mat == 70 :
     print("Mathematics: B2 ")

    elif mat >= 51 or mat == 60 :
     print("Mathematics: C1 ")

    elif mat >= 41 or mat == 50 :
     print("Mathematics: C2 ")

    elif mat >= 35 or mat == 40 :
     print("Mathematics: D ") 

    else :
     print('Mathematics: Fail , needs improvement ')



    if sci >=91 or sci == 100 :
     print("Science: A1 ")

    elif sci >= 81 or sci == 90 :
     print("Science: A2 ")

    elif sci >= 71 or sci == 80 :
     print("Science: B1 ")

    elif sci >= 61 or sci == 70 :
     print("Science: B2 ")

    elif sci >= 51 or sci == 60 :
     print("Science: C1 ")

    elif sci >= 41 or sci == 50 :
     print("Science: C2 ")

    elif sci >= 35 or sci == 40 :
     print("Science: D ") 

    else :
     print('Science: Fail , needs improvement ')



    if soc >=91 or soc == 100 :
     print("Social Science: A1 ")

    elif soc >= 81 or soc == 90 :
     print("Social Science: A2 ")

    elif soc >= 71 or soc == 80 :
     print("Social Science: B1 ")

    elif soc >= 61 or soc == 70 :
     print("Social Science: B2 ")

    elif soc >= 51 or soc == 60 :
     print("Social Science: C1 ")

    elif soc >= 41 or soc == 50 :
     print("Social Science: C2 ")

    elif soc >= 35 or soc == 40 :
     print("Social Science: D ") 

    else :
     print('Social Science: Fail , needs improvement ')
     


if 10 < grade <= 12 :
    stream = input("""Select your stream:
                   Enter 'B' for Biology with Mathematics
                   Enter 'M' for Computer with Mathematics
                   Enter 'P' for computer with Science 
                   Enter 'C' for Commerce
                    """)
    
    if stream.upper() == "B" :
       eng1 = int(input("Enter English mark: "))
       lan1 = int(input("Enter Second Language mark: "))
       mat1 = int(input("Enter Mathematics mark: "))
       bio1 = int(input("Enter Biology mark: "))
       phy1 = int(input("Enter Physics mark: "))
       chem1 = int(input("Enter Chemistry mark: "))
                   
                   
       if eng1 >= 91 or eng1 == 100 :
        print("English: A1 ")
    
       elif eng1 >= 81 or eng1 == 90 :
        print('English: A2 ')

       elif eng1 >= 71 or eng1 == 80 :
        print("English: B1 ")
    
       elif eng1 >= 61 or eng1 == 70 :
        print("English: B2 ")

       elif eng1 >= 51 or eng1 == 60 :
        print("English: C1 ")
    
       elif eng1 >= 41 or eng1 == 50 :
        print("English: C2 ")

       elif eng1 >= 35 or eng1 == 40 :
        print('English: D ')

       else :
        print("English: Fail , needs improvement ")

    
       if lan1 >= 91 or lan1 == 100 :
        print("Second Language: A1 ")
    
       elif lan1 >= 81 or lan1 == 90 :
        print('Second Language: A2 ')

       elif lan1 >= 71 or lan1 == 80 :
        print("Second Language: B1 ")
    
       elif lan1 >= 61 or lan1 == 70 :
        print("Second Language: B2 ")

       elif lan1 >= 51 or lan1 == 60 :
        print("Second Language: C1 ")
    
       elif lan1 >= 41 or lan1 == 50 :
        print("Second Language: C2 ")

       elif lan1 >= 35 or lan1 == 40 :
        print('Second Language: D ')

       else :
        print("Second Language: Fail , needs improvement ")

    
       if mat1 >= 91 or mat1 == 100 :
        print("Mathematics: A1 ")
    
       elif mat1 >= 81 or mat1 == 90 :
        print('Mathematics: A2 ')

       elif mat1 >= 71 or mat1 == 80 :
        print("Mathematics: B1 ")
    
       elif mat1 >= 61 or mat1 == 70 :
        print("Mathematics: B2 ")

       elif mat1 >= 51 or mat1 == 60 :
        print("Mathematics: C1 ")
    
       elif mat1 >= 41 or mat1 == 50 :
        print("Mathematics: C2 ")

       elif mat1 >= 35 or mat1 == 40 :
        print('Mathematics: D ')

       else :
        print("Mathematics: Fail , needs improvement ")


       if bio1 >= 91 or bio1 == 100 :
        print("Biology: A1 ")
    
       elif bio1 >= 81 or bio1 == 90 :
        print('Biology: A2 ')

       elif bio1 >= 71 or bio1 == 80 :
        print("Biology: B1 ")
    
       elif bio1 >= 61 or bio1 == 70 :
        print("Biology: B2 ")

       elif bio1 >= 51 or bio1 == 60 :
        print("Biology: C1 ")
    
       elif bio1 >= 41 or bio1 == 50 :
        print("Biology: C2 ")

       elif bio1 >= 35 or bio1 == 40 :
        print('Biology: D ')

       else :
        print("Biology: Fail , needs improvement ")


       if phy1 >= 91 or phy1 == 100 :
        print("Physics: A1 ")
    
       elif phy1 >= 81 or phy1 == 90 :
        print('Physics: A2 ')

       elif phy1 >= 71 or phy1 == 80 :
        print("Physics: B1 ")
    
       elif phy1 >= 61 or phy1 == 70 :
        print("Physics: B2 ")

       elif phy1 >= 51 or phy1 == 60 :
        print("Physics: C1 ")
    
       elif phy1 >= 41 or phy1 == 50 :
        print("Physics: C2 ")

       elif phy1 >= 35 or phy1 == 40 :
        print('Physics: D ')

       else :
        print("Physics: Fail , needs improvement ")


       if chem1 >= 91 or chem1 == 100 :
        print("Chemistry: A1 ")
    
       elif chem1 >= 81 or chem1 == 90 :
        print('Chemistry: A2 ')

       elif chem1 >= 71 or chem1 == 80 :
        print("Chemistry: B1 ")
    
       elif chem1 >= 61 or chem1 == 70 :
        print("Chemistry: B2 ")

       elif chem1 >= 51 or chem1 == 60 :
        print("Chemistry: C1 ")
    
       elif chem1 >= 41 or chem1 == 50 :
        print("Chemistry: C2 ")

       elif chem1 >= 35 or chem1 == 40 :
        print('Chemistry: D ')

       else :
        print("Chemistry: Fail , needs improvement ")


    
    elif stream.upper() == "M" :
         eng2 = int(input("Enter English mark: "))
         lan2 = int(input("Enter Second Language mark: "))
         mat2 = int(input("Enter Mathematics mark: "))
         it2 = int(input("Enter Information Technology/Practices mark: "))
         phy2 = int(input("Enter Physics mark: "))
         chem2 = int(input("Enter Chemistry mark: "))
         


         if eng2 >= 91 or eng2 == 100 :
          print("English: A1 ")
    
         elif eng2 >= 81 or eng2 == 90 :
          print('English: A2 ')

         elif eng2 >= 71 or eng2 == 80 :
          print("English: B1 ")
    
         elif eng2 >= 61 or eng2== 70 :
          print("English: B2 ")

         elif eng2 >= 51 or eng2 == 60 :
          print("English: C1 ")
    
         elif eng2 >= 41 or eng2 == 50 :
          print("English: C2 ")

         elif eng2 >= 35 or eng2 == 40 :
          print('English: D ')

         else :
          print("English: Fail , needs improvement ")

    
         if lan2 >= 91 or lan2 == 100 :
          print("Second Language: A1 ")
    
         elif lan2 >= 81 or lan2 == 90 :
          print('Second Language: A2 ')

         elif lan2 >= 71 or lan2 == 80 :
          print("Second Language: B1 ")
    
         elif lan2 >= 61 or lan2 == 70 :
          print("Second Language: B2 ")

         elif lan2 >= 51 or lan2 == 60 :
          print("Second Language: C1 ")
    
         elif lan2 >= 41 or lan2 == 50 :
          print("Second Language: C2 ")

         elif lan2 >= 35 or lan2 == 40 :
          print('Second Language: D ')

         else :
          print("Second Language: Fail , needs improvement ")

    
         if mat2 >= 91 or mat2 == 100 :
          print("Mathematics: A1 ")
    
         elif mat2 >= 81 or mat2 == 90 :
          print('Mathematics: A2 ')

         elif mat2 >= 71 or mat2 == 80 :
          print("Mathematics: B1 ")
    
         elif mat2 >= 61 or mat2 == 70 :
          print("Mathematics: B2 ")

         elif mat2 >= 51 or mat2 == 60 :
          print("Mathematics: C1 ")
    
         elif mat2 >= 41 or mat2 == 50 :
          print("Mathematics: C2 ")

         elif mat2 >= 35 or mat2 == 40 :
          print('Mathematics: D ')

         else :
          print("Mathematics: Fail , needs improvement ")


         if it2 >= 91 or it2 == 100 :
          print("Information Technology/Practices: A1 ")
    
         elif it2 >= 81 or it2 == 90 :
          print('Information Technology/Practices: A2 ')

         elif it2 >= 71 or it2 == 80 :
          print("Information Technology/Practices: B1 ")
    
         elif it2 >= 61 or it2 == 70 :
          print("Information Technology/Practices: B2 ")

         elif it2 >= 51 or it2 == 60 :
           print("Information Technology/Practices: C1 ")
    
         elif it2 >= 41 or it2 == 50 :
          print("Information Technology/Practices: C2 ")

         elif it2 >= 35 or it2 == 40 :
          print('Information Technology/Practices: D ')

         else :
          print("Information Technology/Practices: Fail , needs improvement ")


         if phy2 >= 91 or phy2 == 100 :
          print("Physics: A1 ")
    
         elif phy2 >= 81 or phy2 == 90 :
          print('Physics: A2 ')

         elif phy2 >= 71 or phy2 == 80 :
          print("Physics: B1 ")
    
         elif phy2 >= 61 or phy2 == 70 :
          print("Physics: B2 ")

         elif phy2 >= 51 or phy2 == 60 :
          print("Physics: C1 ")
    
         elif phy2 >= 41 or phy2 == 50 :
          print("Physics: C2 ")

         elif phy2 >= 35 or phy2 == 40 :
          print('Physics: D ')

         else :
          print("Physics: Fail , needs improvement ")


         if chem2 >= 91 or chem2 == 100 :
          print("Chemistry: A1 ")
    
         elif chem2 >= 81 or chem2 == 90 :
          print('Chemistry: A2 ')

         elif chem2 >= 71 or chem2 == 80 :
          print("Chemistry: B1 ")
    
         elif chem2 >= 61 or chem2 == 70 :
          print("Chemistry: B2 ")

         elif chem2 >= 51 or chem2 == 60 :
          print("Chemistry: C1 ")
    
         elif chem2 >= 41 or chem2 == 50 :
          print("Chemistry: C2 ")

         elif chem2 >= 35 or chem2 == 40 :
          print('Chemistry: D ')

         else :
          print("Chemistry: Fail , needs improvement ")
    


    elif stream.upper() == "P" :
         eng3 = int(input("Enter English mark: "))
         lan3 = int(input("Enter Second Language mark: "))
         it3 = int(input("Enter Information Technology/Practices mark: "))
         bio3 = int(input("Enter Biology mark: "))
         phy3 = int(input("Enter Physics mark: "))
         chem3 = int(input("Enter Chemistry mark: "))


         if eng3 >= 91 or eng3 == 100 :
          print("English: A1 ")
    
         elif eng3 >= 81 or eng3 == 90 :
          print('English: A2 ')

         elif eng3 >= 71 or eng3 == 80 :
          print("English: B1 ")
    
         elif eng3 >= 61 or eng3 == 70 :
          print("English: B2 ")

         elif eng3 >= 51 or eng3 == 60 :
          print("English: C1 ")
    
         elif eng3 >= 41 or eng3 == 50 :
          print("English: C2 ")

         elif eng3 >= 35 or eng3 == 40 :
          print('English: D ')

         else :
          print("English: Fail , needs improvement ")

    
         if lan3 >= 91 or lan3 == 100 :
          print("Second Language: A1 ")
    
         elif lan3 >= 81 or lan3 == 90 :
          print('Second Language: A2 ')

         elif lan3 >= 71 or lan3 == 80 :
          print("Second Language: B1 ")
    
         elif lan3 >= 61 or lan3 == 70 :
          print("Second Language: B2 ")

         elif lan3 >= 51 or lan3 == 60 :
          print("Second Language: C1 ")
    
         elif lan3 >= 41 or lan3 == 50 :
          print("Second Language: C2 ")

         elif lan3 >= 35 or lan3 == 40 :
          print('Second Language: D ')

         else :
          print("Second Language: Fail , needs improvement ")

    
         if it3 >= 91 or it3 == 100 :
          print("Information Technology/Practices: A1 ")
    
         elif it3 >= 81 or it3== 90 :
          print('Information Technology/Practices: A2 ')

         elif it3 >= 71 or it3 == 80 :
          print("Information Technology/Practices: B1 ")
    
         elif it3 >= 61 or it3 == 70 :
          print("Information Technology/Practices: B2 ")

         elif it3 >= 51 or it3 == 60 :
          print("Information Technology/Practices: C1 ")
    
         elif it3 >= 41 or it3 == 50 :
          print("Information Technology/Practices: C2 ")

         elif it3 >= 35 or it3 == 40 :
          print('Information Technology/Practices: D ')

         else :
          print("Information Technology/Practices: Fail , needs improvement ")


         if bio3 >= 91 or bio3 == 100 :
          print("Biology: A1 ")
    
         elif bio3 >= 81 or bio3 == 90 :
          print('Biology: A2 ')

         elif bio3 >= 71 or bio3 == 80 :
          print("Biology: B1 ")
    
         elif bio3 >= 61 or bio3 == 70 :
          print("Biology: B2 ")

         elif bio3 >= 51 or bio3 == 60 :
          print("Biology: C1 ")
    
         elif bio3 >= 41 or bio3 == 50 :
          print("Biology: C2 ")

         elif bio3 >= 35 or bio3 == 40 :
          print('Biology: D ')

         else :
          print("Biology: Fail , needs improvement ")


         if phy3 >= 91 or phy3 == 100 :
          print("Physics: A1 ")
    
         elif phy3 >= 81 or phy3 == 90 :
          print('Physics: A2 ')

         elif phy3 >= 71 or phy3 == 80 :
          print("Physics: B1 ")
    
         elif phy3 >= 61 or phy3 == 70 :
          print("Physics: B2 ")

         elif phy3 >= 51 or phy3 == 60 :
          print("Physics: C1 ")
    
         elif phy3 >= 41 or phy3 == 50 :
          print("Physics: C2 ")

         elif phy3 >= 35 or phy3 == 40 :
          print('Physics: D ')

         else :
          print("Physics: Fail , needs improvement ")


         if chem3 >= 91 or chem3 == 100 :
          print("Chemistry: A1 ")
    
         elif chem3 >= 81 or chem3 == 90 :
          print('Chemistry: A2 ')

         elif chem3 >= 71 or chem3 == 80 :
          print("Chemistry: B1 ")
    
         elif chem3 >= 61 or chem3 == 70 :
          print("Chemistry: B2 ")

         elif chem3 >= 51 or chem3 == 60 :
          print("Chemistry: C1 ")
    
         elif chem3 >= 41 or chem3 == 50 :
          print("Chemistry: C2 ")

         elif chem3 >= 35 or chem3 == 40 :
          print('Chemistry: D ')

         else :
          print("Chemistry: Fail , needs improvement ")


    elif stream.upper() == "C" :
         eng4 = int(input("Enter English mark: "))
         lan4 = int(input("Enter Second Language mark: "))
         acc4 = int(input("Enter Accountancy mark: "))
         Busi4 = int(input("Enter Business Studies mark: "))
         eco4 = int(input("Enter Economics mark: "))
         opt4 = input(""" Select your opted subject: 
                     Enter 'I' for Information Practices 
                     Enter 'H' for Mathematics 
                     Enter 'P' for Physical Education 
                      """)
         
         if opt4.upper() == "I" :
            ip4 = int(input('Enter Information Practices mark: '))
            if ip4 >= 91 or ip4 == 100 :
              print("Information Practices: A1 ")
    
            elif ip4 >= 81 or ip4 == 90 :
             print('Information Practices: A2 ')

            elif ip4 >= 71 or ip4 == 80 :
             print("Information Practices: B1 ")
    
            elif ip4 >= 61 or ip4 == 70 :
             print("Information Practices: B2 ")

            elif ip4 >= 51 or ip4 == 60 :
             print("Information Practices: C1 ")
    
            elif ip4 >= 41 or ip4 == 50 :
             print("Information Practices: C2 ")

            elif ip4 >= 35 or ip4 == 40 :
             print('Information Practices: D ')

            else :
             print("Information Practices: Fail , needs improvement ")

         if opt4.upper() == "H" :
            mat4 = int(input('Enter Mathematics mark: '))
            if mat4 >= 91 or mat4 == 100 :
             print("Mathematics: A1 ")
    
            elif mat4 >= 81 or mat4 == 90 :
             print('Mathematics: A2 ')

            elif mat4 >= 71 or mat4 == 80 :
             print("Mathematics: B1 ")
    
            elif mat4 >= 61 or mat4 == 70 :
             print("Mathematics: B2 ")

            elif mat4 >= 51 or mat4 == 60 :
             print("Mathematics: C1 ")
    
            elif mat4 >= 41 or mat4 == 50 :
             print("Mathematics: C2 ")

            elif mat4 >= 35 or mat4 == 40 :
             print('Mathematics: D ')

            else :
             print("Mathematics: Fail , needs improvement ")

         if opt4.upper() == "P" :
            pe4 = int(input('Enter Physical Education: '))
            if pe4 >= 91 or pe4 == 100 :
             print("Physical Education: A1 ")
    
            elif pe4 >= 81 or pe4 == 90 :
             print('Physical Education: A2 ')

            elif pe4 >= 71 or pe4 == 80 :
             print("Physical Education: B1 ")
    
            elif pe4 >= 61 or pe4 == 70 :
             print("Physical Education: B2 ")

            elif pe4 >= 51 or pe4 == 60 :
             print("Physical Education: C1 ")
    
            elif pe4 >= 41 or pe4 == 50 :
             print("Physical Education: C2 ")

            elif pe4 >= 35 or pe4 == 40 :
              print('Physical Education: D ')

            else :
             print("Physical Education: Fail , needs improvement ")



         if eng4 >= 91 or eng4 == 100 :
          print("English: A1 ")
    
         elif eng4 >= 81 or eng4 == 90 :
          print('English: A2 ')

         elif eng4 >= 71 or eng4 == 80 :
          print("English: B1 ")
    
         elif eng4 >= 61 or eng4 == 70 :
          print("English: B2 ")

         elif eng4 >= 51 or eng4 == 60 :
          print("English: C1 ")
    
         elif eng4 >= 41 or eng4 == 50 :
          print("English: C2 ")

         elif eng4 >= 35 or eng4 == 40 :
          print('English: D ')

         else :
          print("English: Fail , needs improvement ")

    
         if lan4 >= 91 or lan4 == 100 :
          print("Second Language: A1 ")
    
         elif lan4 >= 81 or lan4 == 90 :
          print('Second Language: A2 ')

         elif lan4 >= 71 or lan4 == 80 :
          print("Second Language: B1 ")
    
         elif lan4 >= 61 or lan4 == 70 :
          print("Second Language: B2 ")

         elif lan4 >= 51 or lan4 == 60 :
          print("Second Language: C1 ")
    
         elif lan4 >= 41 or lan4 == 50 :
          print("Second Language: C2 ")

         elif lan4 >= 35 or lan4 == 40 :
          print('Second Language: D ')

         else :
          print("Second Language: Fail , needs improvement ")


         if acc4 >= 91 or acc4 == 100 :
          print("Accountancy: A1 ")
    
         elif acc4 >= 81 or acc4 == 90 :
          print('Accountancy: A2 ')

         elif acc4 >= 71 or acc4 == 80 :
          print("Accountancy: B1 ")
    
         elif acc4 >= 61 or acc4 == 70 :
          print("Accountancy: B2 ")

         elif acc4 >= 51 or acc4 == 60 :
          print("Accountancy: C1 ")
    
         elif acc4 >= 41 or acc4 == 50 :
          print("Accountancy: C2 ")

         elif acc4 >= 35 or acc4 == 40 :
          print('Accountancy: D ')

         else :
          print("Accountancy: Fail , needs improvement ")


         if Busi4 >= 91 or Busi4 == 100 :
          print("Business Studies: A1 ")
    
         elif Busi4 >= 81 or Busi4 == 90 :
          print('Business Studies: A2 ')

         elif Busi4 >= 71 or Busi4 == 80 :
          print("Business Studies: B1 ")
    
         elif Busi4 >= 61 or Busi4 == 70 :
          print("Business Studies: B2 ")

         elif Busi4 >= 51 or Busi4 == 60 :
          print("Business Studies: C1 ")
    
         elif Busi4 >= 41 or Busi4 == 50 :
          print("Business Studies: C2 ")

         elif Busi4 >= 35 or Busi4 == 40 :
          print('Business Studies: D ')

         else :
          print("Business Studies: Fail , needs improvement ")


         if eco4 >= 91 or eco4 == 100 :
          print("Economics: A1 ")
    
         elif eco4 >= 81 or eco4 == 90 :
          print('Economics: A2 ')

         elif eco4 >= 71 or eco4 == 80 :
          print("Economics: B1 ")
    
         elif eco4 >= 61 or eco4 == 70 :
          print("Economics: B2 ")

         elif eco4 >= 51 or eco4 == 60 :
          print("Economics: C1 ")
    
         elif eco4 >= 41 or eco4 == 50 :
          print("Economics: C2 ")

         elif eco4 >= 35 or eco4 == 40 :
          print('Economics: D ')

         else :
          print("Economics: Fail , needs improvement ")


else :
  print('Enter your grade correctly ! ')
         

