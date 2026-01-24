# 🎓 Student Management System (CLI)

A command-line based Student Management System built using Python.  
This project demonstrates Object-Oriented Programming (OOP), CSV file handling, input validation, and full CRUD operations.

---

## ✨ Features

- ➕ Add student records  
- 📄 View all students  
- 🔍 Search students by ID or name  
- ✏️ Update student details (department or marks)  
- 🗑️ Delete student records with confirmation  
- 💾 Persistent storage using CSV files  
- 🔒 Student ID uniqueness enforcement  
- ✅ Input validation for numeric marks  

---

## 🧠 Design Overview

- **students_list** acts as the in-memory source of truth during program execution.
- The CSV file is used only for persistence between program runs.
- Data Flow:
  - CSV → DictReader → Student objects → `students_list`
  - `students_list` → dict → CSV (on save)
- CSV overwrite does **not** cause data loss because all data exists in memory before saving.

---

## 🛠️ Technologies Used

- Python
- CSV module
- Object-Oriented Programming (OOP)

---

## 🚀 How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run the program:
   ```bash
   python student_management_system.py
   ```
4. Follow the on-screen menu options


## 📌 Notes

- Designed as a Semester 1 foundational project
- Focuses on correctness, clarity, and system-level thinking
- CLI-based to strengthen core logic and validation handling
