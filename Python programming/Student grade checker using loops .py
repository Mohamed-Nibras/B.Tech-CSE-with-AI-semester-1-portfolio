#title 
print('\n' + "=" * 173)
print('\n'+'STUDENT GRADE CHECKER WITH PROGRESS CARD'.center(173,'-'))
print('\n' + '=' * 173)
#name and grade

name = input('\nEnter your name: ')
std = int(input('\nEnter your grade: '))
schl = input('\nEnter your school name: ')
while not 3 <= len(name) <= 50 or not  1 <= std <= 12 or schl == '' :
    print('\nName should be between 3 to 50 characters'
          '\nGrade must be in numbers and between 1 and 12 '
          '\nEnter School name correctly ')
    name = input('\nEnter your name: ')
    std = int(input('\nEnter your grade: '))
    schl = input('\nEnter your school name: ')

print('\n' \
f'\nNAME: {name} '
f'\nSTANDARD: {std} '
f'\nSCHOOL: {schl} ')

#grade and stream
while True :
 if std <= 10 :
      subjects = ['English']
      sec_lang = input("\nEnter your Second Language (Press Enter to skip): ")
      if sec_lang != '':
          subjects.append(sec_lang)
      subjects.extend(["Mathematics", "Science", "Social Science"])
      break

 elif std in [11,12] :
     stream = input(
  '\nEnter your stream: \n'
  "\n'BIOMATHS' for Biology with Mathematics"
  "\n'COMPUTER MATHS' for Computer with Mathematics"
  "\n'PURE SCIENCE' for Pure Science"
  "\n'COMMERCE' for Commerce "
  "\n> ").upper()

     if stream == 'BIOMATHS':
          subjects = ['English']
          sec_lang = input("\nEnter your Second Language (Press Enter to skip): ").strip()
          if sec_lang != "":
              subjects.append(sec_lang)
          subjects.extend(['Biology','Mathematics','Physics','Chemistry'])
          break
          
     elif stream == 'COMPUTER MATHS' :
          subjects = ["English"]
          sec_lang = input("\nEnter your Second Language (Press Enter to skip): ").strip()
          if sec_lang != "":
              subjects.append(sec_lang)
          subjects.extend(["Computer Science","Mathematics","Physics","Chemistry"])
          break

     elif stream == 'PURE SCIENCE' :
          subjects = ["English"]
          sec_lang = input("\nEnter your Second Language (Press Enter to skip): ").strip()
          if sec_lang != "":
              subjects.append(sec_lang)
          subjects.extend(["Computer Science","Biology","Chemistry","Physics"])
          break

     elif stream == 'COMMERCE' :
          subjects = ["English"]
          sec_lang = input("\nEnter your Second Language (Press Enter to skip): ").strip()
          if sec_lang != "":
              subjects.append(sec_lang)
          subjects.extend(["Business Studies", "Economics"])
          opt_subject = input('Enter your optional subject(Press Enter to skip): ')
          if opt_subject != '':
               subjects.append(opt_subject)
               break

          else :
               break
               

     else :
          print('\nInvalid stream ')
          subjects =[]

print('\nYour subjects are: ')
for sub in subjects:
    print(sub)

#marks entering

subject_marks = []

for sub in subjects :
    while True:
        marks_input = input(f'\nEnter your {sub} marks: ')

        if not marks_input.isdigit():
            print('\nEnter valid marks ! ')
            continue
        mark = int(marks_input)

        if 0 <= mark <= 100 :
            subject_marks.append(mark)
            break
        
        else :
            print('\nMarks must be between 0 to 100')



#marks display and grade


grades = [ ]

for i in range(len(subjects)) :
    mark = subject_marks[i]
    grade = ''
    if 91 <= mark <= 100:
        grade = "A1"
    elif 81 <= mark <= 90:
        grade = "A2"
    elif 71 <= mark <= 80:
        grade = "B1"
    elif 61 <= mark <= 70:
        grade = "B2"
    elif 51 <= mark <= 60:
        grade = "C1"
    elif 41 <= mark <= 50:
        grade = "C2"
    elif 35 <= mark <= 40:
        grade = "D"
    else:
        grade = "Fail, needs improvement"

    grades.append(grade)

# extra
total = 0
for sum_score in subject_marks:
    total += sum_score
maxtotal = len(subjects) * 100

average = total / len(subjects)
if average >= 90:
    avg_grade = "A+"
elif average >= 80:
    avg_grade = "A"
elif average >= 70:
    avg_grade = "B"
elif average >= 60:
    avg_grade = "C"
elif average >= 50:
    avg_grade = "D"
else:
    avg_grade = "Fail"

if any (mark < 35 for mark in subject_marks):
    result = 'FAIL ❌'

else: 
    result = 'PASS ✅'


#final progress card 
print('\n' + "=" * 173)
print('\n'+'STUDENT PROGRESS CARD'.center(173,'-'))
print('\n' + '=' * 173)
print(f'\nSTUDENT NAME: {name}')
print(f'\nSTANDARD: {std}')
if std in [11,12]:
    print(f'\nSTREAM: {stream}')
print(f'\nSUBJECT WISE REPORT 👇')
for i in range(len(subjects)):
  print(f'\nSUBJECT: {subjects[i]}; MARK: {subject_marks[i]} ---> GRADE: {grades[i]}')
print(f'\nTOTAL MARKS: {total}/{maxtotal}')
print(f'\nMARK AVERAGE: {average:.2f}')
print(f'\nGRADE AVERAGE: {avg_grade}')
print(f'\nRESULT: {result}')
print(f'\n'
      'Yours Respectfully ,' \
     f'{schl}')