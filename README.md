# School Management System

Welcome to the **School Management System**, a Python-based application designed to streamline and automate essential administrative functions of a school, including managing student and teacher records, attendance tracking, and financial operations like salary and fee payments.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Customization Guide](#customization-guide)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Features
- **Student and Teacher Records Management**: Add, update, delete, and view data.
- **Attendance Tracking**: Monitor and manage attendance records for students and teachers.
- **Fees and Salaries Management**: Record and track financial transactions efficiently.
- **Menu-Driven Interface**: Simple and interactive terminal-based navigation.
- **Database Integration**: Ensures persistence and reliability of data using MySQL.

---

## Technologies Used
- **Python**: Core application logic and scripting.
- **MySQL**: Backend database for storing and retrieving information.
- **mysql-connector-python**: Library for database communication.

---

## File Structure
```
school-management-system/
│
├── SchoolManagement.py(main)    # Entry point of the application
├── Sm.py                        # Core module integrating student, teacher, attendance, fees, and salary
├── Student.py                   # Student management logic
├── Teacher.py                   # Teacher management logic
├── Studentattendance.py         # Student attendance management
├── Teacherattendance.py         # Teacher attendance management
├── PayFees.py                   # Fees payment management
├── PaySalary.py                 # Salary payment management
├── requirements.pdf             # (Code for creating databases and tables)
└── README.md                    # Project documentation (this file)
```

---

## Setup Instructions
1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd school-management-system
   ```

2. . **Set Up the Database**  
   Create a database named `csproject` and run SQL commands to create necessary tables. Refer to the project content (requirements.pdf) for table structures.

4. **Run the Application**  
   ```bash
   python main.py
   ```

---

## How to Use
1. **Navigate through the Menu**  
   - Choose options (1–7) for managing students, teachers, attendance, fees, or salaries.
   - Follow prompts to perform actions like adding or deleting records.

2. **Database Configuration**  
   - Update database connection details in each `.py` file (e.g., host, user, password).

3. **Sample Operations**  
   - Add a student: Select "Student Record" → "Insert Student Record."
   - View teacher attendance: Select "Teacher Attendance Records" → "Show Records."

---

## Customization Guide
1. **Modify Features**  
   Extend functionalities in respective files (e.g., `Student.py` or `Teacherattendance.py`).

2. **Change Database**  
   Update database connection credentials in all Python scripts to align with your MySQL setup.

3. **Enhance User Interface**  
   Replace the terminal-based menu with a graphical interface using libraries like `Tkinter` or `PyQt`.

---

## Acknowledgments
This project was developed as part of the CBSE AISSCE 2021 coursework. Special thanks to mentors, peers, and online communities for their guidance and support.

---

## Contact
For queries or suggestions, please reach out via email: **tjalan@asu.edu**  
