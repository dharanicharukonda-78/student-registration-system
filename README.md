# Student Registration System

## Project Overview

This project is a simple Student Registration System developed using Python Tkinter and SQLite.

It collects student details through a graphical user interface (GUI) and stores the information in an SQLite database.

## Technologies Used

* Python
* Tkinter (Frontend / GUI)
* SQLite (Database)
* Python sqlite3 module (Database connectivity)

## Complete Project Flow

**Step 1: Frontend — Tkinter UI**
The student enters their Name, Email, Mobile Number, College Name, and Course in the registration form.

**Step 2: Backend — Python**
Python collects the entered information using the form fields and processes it when the Register button is clicked.

**Step 3: Database Connectivity**
Python connects to the SQLite database using the `sqlite3` module.

**Step 4: Database Insert**
The registration details are inserted into the `registrations` table in `registration.db`.

### Application Flow

Student enters details
↓
Tkinter Registration Form (UI)
↓
Python Registration Function (Backend)
↓
SQLite Database Connection
↓
INSERT INTO registrations
↓
Student details saved in the database

## Database Details

* Database file: `registration.db`
* Table name: `registrations`
* Fields: ID, Name, Email, Mobile, College, Course

## How to Run the Project

1. Install Python on your computer.

2. Download or clone this repository.

3. Open the project folder in VS Code.

4. Open the terminal in the project folder.

5. Run the command:

   `python main.py`

6. Enter the student details in the registration form.

7. Click the Register button.

8. Verify that the registration details are saved in the SQLite database.

## How to Verify Database Records

Run this command in the project terminal:

`python -c "import sqlite3; c=sqlite3.connect('registration.db'); print(c.execute('SELECT * FROM registrations').fetchall()); c.close()"`

The command displays the records stored in the database.

## Expected Result

The registration form opens, Python processes the submitted details, and the information is stored in the SQLite database.

## Author

Dharani Charukonda
