# Upgraded student grade checker

# Title
import shutil
width = shutil.get_terminal_size().columns
print("=" * width)
print("STUDENT GRADE CHECKER".center(width))
print("=" * width)

# Name entry

def name_validator():
    while True:
        entry = {
            "Name" : input("Enter your name (3 to 50 characters): ").strip(),
            "Standard" : input("Enter your standard (1 to 12): ").strip(),
            "School" : input("Enter your school name: ").strip()
        }

        if not (3 <= len(entry['Name']) <= 50):
            print("❌ Name must be between 3 to 50 characters ")
            continue
        
        if not entry['Standard'].isdigit():
            print("❌ Standard must be a number between 1 to 12 ")
            continue

        entry["Standard"] = int(entry["Standard"])
        
        if not (1 <= entry["Standard"] <= 12):
            print("❌ Standard must be a number between 1 to 12 ")
            continue

        if entry['School'] == "":
            print("❌ Enter appropriate school name ")
            continue

        print('\n'
              f"\n NAME: {entry['Name']}"
              f"\n STANDARD: {entry['Standard']}"
              f"\n SCHOOL: {entry['School']}")
        
        return entry
    
# Grade and stream checking

def grade_stream_evaluator(entry):

        if entry["Standard"] <= 10:
            subjects = ["English"]
            
            subjects.extend(['Mathematics', 'Science', 'Social Science'])
            
            return subjects
        
        elif entry["Standard"] in [11, 12]:
            while True:
                stream = input(
  '\nEnter your stream: \n'
  "\n'BIOMATHS' for Biology with Mathematics"
  "\n'COMPUTER MATHS' for Computer with Mathematics"
  "\n'PURE SCIENCE' for Pure Science"
  "\n'COMMERCE' for Commerce "
  "\n> ").upper()
                
                if stream == "BIOMATHS":
                    subjects = ["English"]
                    
                    subjects.extend(['Mathematics', 'Biology', 'Physics', 'Chemistry'])
            
                    return subjects, stream
                
                elif stream == "COMPUTER MATHS":
                    subjects = ["English"]
                    
                    subjects.extend(['Mathematics', 'Computer Science', 'Physics', 'Chemistry'])
            
                    return subjects, stream
                
                elif stream == "PURE SCIENCE":
                    subjects = ["English"]
                    
                    subjects.extend(['Biology', 'Computer Science', 'Physics', 'Chemistry'])
            
                    return subjects, stream
                
                elif stream == "COMMERCE":
                    subjects = ["English"]
                    
                    subjects.extend(['Business Studies', 'Economics'])
                    optional_subject = input("Enter your Optional Subject(Press ENTER to skip): ").strip()
                    if optional_subject != '':
                        subjects.append(optional_subject)
                    
            
                    return subjects, stream
                
                else:
                    print("❌ Invalid stream, enter appropriate stream ")
                    
# Adding additional and second languages

def second_language_and_additional_subjects(subjects: list):
    second_language = input("Enter your Second Language(Press ENTER to skip): ").strip()
    if second_language != '':
        subjects.insert(1, second_language)
            
    additional_subject = input("Enter your Additonal Subject(Press ENTER to skip): ").strip()
    if additional_subject != '':
        subjects.append(additional_subject)

    
    return subjects

# Inputing marks for the subject

def mark_input_evaluator(subjects):
    subject_marks = []

    for sub in subjects:
        while True:
            marks_input = input(f"\n Enter your {sub} marks: ")

            if not marks_input.isdigit():
                print("\n Marks must be numbers ")
                continue
            mark = int(marks_input)

            if not (0 <= mark <= 100):
                print("\n Marks must be between 0 to 100 ")
                continue

            else:
                subject_marks.append(mark)
                break

    return subject_marks
            
# Grades

def grade_calculation(subjects, subject_marks):
    grades = []

    for i in range(len(subjects)):
        mark = subject_marks[i]

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

    return grades

# Extra for progress card

def extra_calculations(subject_marks, subjects):
    
    total = 0
    for sum_score in subject_marks:
        total += sum_score

    maxtotal = len(subjects) * 100
    average = total / len(subjects)

    if average >= 90:
        avg_grade = "A1"
    elif average >= 80:
        avg_grade = "A2"
    elif average >= 70:
        avg_grade = "B1"
    elif average >= 60:
        avg_grade = "B2"
    elif average >= 50:
        avg_grade = "C1"
    elif average >= 40:
        avg_grade = "C2"
    elif average >= 35:
        avg_grade = "D"
    else:
        avg_grade = "Fail"

    if any(mark < 35 for mark in subject_marks):
        result = "Fail ❌"
    else:
        result = "Pass ✅"

    return total, maxtotal, average, avg_grade, result

# Progress card

def printing_progress_card(entry, subjects, subject_marks, grades, total, maxtotal, average, avg_grade, result, stream = None):

    print("=" * width)
    print("PROGRESS CARD".center(width))
    print("=" * width)
    
    print(f"\nSTUDENT NAME: {entry['Name']}")
    print(f"\nSTANDARD: {entry['Standard']}")
    if entry['Standard'] in [11,12]:
        print(f"\nSTREAM: {stream}")
    print("\n")
    print("-" * width)
    print(f"SUBJECT WISE REPORT".center(width))
    print(("-" * 19) .center(width))
    for i in range(len(subjects)):
        print(f'\nSUBJECT: {subjects[i]}; MARK: {subject_marks[i]} ---> GRADE: {grades[i]}')
    print("\n")
    print("-" * width)
    print(f"MARKS REPORT".center(width))
    print(("-" * 12) .center(width))
    print(f'\nTOTAL MARKS: {total}/{maxtotal}')
    print(f'\nMARK AVERAGE: {average:.2f}')
    print(f'\nGRADE AVERAGE: {avg_grade}')
    print(f'\nRESULT: {result}')
    print(f'\n'
      'Yours Respectfully ,' \
     f"{entry['School']}")
    
# Mainfunction calling

def main():
    entry = name_validator()

    if entry["Standard"] <= 10:
        subjects = grade_stream_evaluator(entry)
        stream = None
    else:
        subjects, stream = grade_stream_evaluator(entry)

    subjects = second_language_and_additional_subjects(subjects)
    subject_marks = mark_input_evaluator(subjects)
    grades = grade_calculation(subjects, subject_marks)

    total, maxtotal, average, avg_grade, result = extra_calculations(subject_marks, subjects)

    printing_progress_card(
        entry, subjects, subject_marks, grades,
        total, maxtotal, average, avg_grade, result, stream
    )

main()