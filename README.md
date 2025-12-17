# Student Management System (Python)

A simple command-line based Student Management System built using Python.  
The application allows users to add, view, and search student records with persistent storage using file handling.

---

## Features
- Add student records (roll number, name, marks)
- View all stored students
- Search a student by roll number
- Persistent storage using a text file
- Automatic creation of the data file if it does not exist

---

## How It Works
- Student data is stored in a text file (`students.txt`)
- Each record is stored using the format `roll,name,marks`
- Data is loaded into memory using a list of dictionaries
- The program handles missing data files by creating them automatically

---

## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run the program:

```bash
python student_manager.py

