"""
Student Management System (CLI)

Features:
- Add, View, Search, Update, Delete students
- CSV-based persistent storage
- ID uniqueness enforcement
- Input validation for marks
- OOP-based data representation

Note:
- students_list is the source of truth during runtime
- CSV is used only for persistence between runs
"""


import shutil
import csv
width = shutil.get_terminal_size().columns
print("=" * width)
print("\n")
print("STUDENT MANAGEMENT SYSTEM 🎓".center(width))
print(("-" * 27).center(width))
print("\n")
print("=" * width)

# -------------------- DATA MODEL --------------------
class Student:
    def __init__ (self, student_id, name, department, marks):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.marks = marks

# In-memory storage (source of truth during program execution)
students_list = []

# -------------------- FILE HANDLING (CSV) --------------------
def load_students():  # Runs once at program start ( line 212 )
    # Loads student data from CSV into memory (students_list)
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            # CSV -> dict -> Student object -> list
            for row in reader:
                student = Student(
                    row["id"],
                    row["name"],
                    row["department"],
                    row["marks"]
                )
                students_list.append(student)

    except FileNotFoundError:
        pass

# -------------------- FILE HANDLING (CSV) --------------------
def save_students():# Saves current in-memory student data back to CSV
        # Overwrites the file using students_list as the source of truth
        with open("students.csv", "w", newline="") as file:
            fieldnames = ["id", "name", "department", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            # list -> student object -> dict -> csv
            for student in students_list:
                writer.writerow({
                    "id": student.student_id,
                    "name": student.name,
                    "department": student.department,
                    "marks": student.marks,
                })

    
# CONCEPT NOTE:
# - students_list is the main working data during program execution
# - CSV file is only a snapshot for persistence
# - Data flow:
#   CSV -> DictReader -> Student objects -> students_list
#   students_list -> dict -> CSV (on save)
# - CSV overwrite does NOT cause data loss because memory holds all data



# -------------------- CORE FUNCTIONALITY --------------------
def show_menu():
    print("-" * width)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("-" * width)

# Adds a new student after validating:
def add_student():
    # - Unique student ID
    while True:
        student_id = input("\nEnter Student ID: ").strip()
        duplicate = False
        for student in students_list:
            if student.student_id == student_id:
                print("\n❌ Student ID already exist. Enter a New ID")
                duplicate = True
                break
        if not duplicate:
           break
    name = input("Enter Student name: ").strip()
    department = input("Enter Student's department: ").strip()
    # - Numeric marks
    while True:
        marks = input("Enter Student's marks: ").strip()
        if marks.isdigit():
            break
        else:
            print("\n❌ Marks must be in numbers ")

    # Updates both memory and CSV
    student_details = Student(student_id, name, department, marks)
    students_list.append(student_details)
    save_students()
    print("\n✅ Student added successfully")



def view_students():

    if not students_list:
        print("\n⚠️ No students available")
        return
    else:
        print("\n")
        print("~" * width)
        print("\n")
        print("STUDENT LIST".center(width))
        print(("-" * 12).center(width))
        print("\n")

        for student in students_list:
            print(
                f"ID: {student.student_id} | "
                f"NAME: {student.name} | "
                f"DEPARTMENT: {student.department} | "
                f"MARKS: {student.marks} | "
            )

# Searches student by ID or Name (case-insensitive)
def search_student():
    # Reads from memory only (no file access)
    if not students_list:
        print("\n⚠️ No students available")
        return
    
    else:

        keyword = input("Enter Student's ID or NAME to search 🔎: ").strip().lower()
        found = False

        for student in students_list:
            if student.student_id == keyword or student.name.lower() == keyword:
                print("\n✅ Student found ")
                print(
                    f"ID: {student.student_id} | "
                    f"NAME: {student.name} | "
                    f"DEPARTMENT: {student.department} | "
                    f"MARKS: {student.marks} | "
                )
                found = True
                break
        
        if not found:
            print("\n⚠️ Student NOT FOUND ")

# Updates department or marks for a given student ID
def update_student():
    if not students_list:
        print("\n⚠️ No students available")
        return
    
    student_id = input("\nEnter Student ID to update: ").strip()
    for student in students_list:
        if student.student_id == student_id:
            print("\n Choose options for update ")
            print("1. Department")
            print("2. Marks")

            choice = input("Enter options ( 1 or 2 ): ").strip()

            if choice == "1":
                new_department = input("Enter New Department: ").strip()
                student.department = new_department
            elif choice == "2":
                new_marks = input("Enter New Marks: ").strip()
                student.marks = new_marks
            else:
                print("❌ Invalid option. Choose option from menu ")
                return
            # Changes are saved immediately to CSV
            save_students()
            print("✅ Student Updated Successfully ")
            return
        
    print("\n⚠️ Student not found ")

# Deletes a student after confirmation
def delete_student():
    if not students_list:
        print("\n⚠️ No students available")
        return
    
    student_id = input("Enter Student ID or NAME to delete: ").strip().lower()
    for student in students_list:
        if student.student_id == student_id or student.name.lower() == student_id:
            print("\n Student found ✅")
            print(
                    f"ID: {student.student_id} | "
                    f"NAME: {student.name} | "
                    f"DEPARTMENT: {student.department} | "
                    f"MARKS: {student.marks} | "
                )
            
            confirm = input("\nAre you sure you want to delete this Student ❔ Yes/No: ").strip().lower()
            # Removes from memory and updates CSV
            if confirm == "yes":
                students_list.remove(student)
                save_students()
                print("\n🗑️✅ Student Removed Successfully ")
            else:
                print("\n🗑️❌ Deletion Cancelled ")
            return
            
    print("\n⚠️ Student not found ")

            

 # Runs once at program start 
load_students()

while True:
    print("\n")
    show_menu()
    choice = input("Choose an option ( 1 to 6 ): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice =="5":
        delete_student()
    elif choice == "6":
        print("\nExiting...⌛")
        print("✅ DONE")
        break
    else:
        print("\n❌ Invalid option. Choose option from menu ")