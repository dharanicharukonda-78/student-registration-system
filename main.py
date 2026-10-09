
import tkinter as tk
from tkinter import messagebox
import sqlite3


# DATABASE CONNECTION
def connect_database():
    connection = sqlite3.connect("registration.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile TEXT NOT NULL,
            college TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# BACKEND: REGISTER STUDENT
def register_student():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    mobile = mobile_entry.get().strip()
    college = college_entry.get().strip()
    course = course_entry.get().strip()

    if not all([name, email, mobile, college, course]):
        messagebox.showwarning(
            "Missing Details",
            "Please fill in all fields."
        )
        return

    try:
        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO registrations
            (name, email, mobile, college, course)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, mobile, college, course))

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success",
            "Student registered successfully!"
        )

        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        mobile_entry.delete(0, tk.END)
        college_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)

    except sqlite3.Error as error:
        messagebox.showerror("Database Error", str(error))


# FRONTEND: CREATE WINDOW
connect_database()

root = tk.Tk()
root.title("Student Registration System")
root.geometry("500x520")
root.configure(bg="#eef2f7")
root.resizable(False, False)

heading = tk.Label(
    root,
    text="STUDENT REGISTRATION",
    font=("Arial", 18, "bold"),
    bg="#243b55",
    fg="white",
    pady=18
)
heading.pack(fill="x")

form = tk.Frame(root, bg="#eef2f7", padx=40, pady=20)
form.pack(fill="both", expand=True)


def add_field(label_text, row):
    label = tk.Label(
        form,
        text=label_text,
        font=("Arial", 11, "bold"),
        bg="#eef2f7",
        anchor="w"
    )
    label.grid(row=row, column=0, sticky="w", pady=7)

    entry = tk.Entry(
        form,
        font=("Arial", 11),
        width=28,
        relief="solid",
        bd=1
    )
    entry.grid(row=row, column=1, ipady=5, pady=7)

    return entry


name_entry = add_field("Name:", 0)
email_entry = add_field("Email:", 1)
mobile_entry = add_field("Mobile Number:", 2)
college_entry = add_field("College:", 3)
course_entry = add_field("Course:", 4)

register_button = tk.Button(
    form,
    text="REGISTER",
    command=register_student,
    font=("Arial", 12, "bold"),
    bg="#243b55",
    fg="white",
    activebackground="#365b7d",
    activeforeground="white",
    width=20,
    pady=8,
    cursor="hand2"
)
register_button.grid(
    row=5, column=0, columnspan=2, pady=25
)

root.mainloop()