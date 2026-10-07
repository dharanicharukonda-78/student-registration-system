import tkinter as tk
import sqlite3
connection = sqlite3.connect("registration.db")
connection.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    mobile TEXT,
    college TEXT,
    course TEXT
)
""")

connection.commit()
window = tk.Tk()
window.title("Student Registration")
def register():
    name = name_Entry.get()
    email = email_Entry.get()
    mobile = mobile_Entry.get()
    college = college_Entry.get()
    course = course_Entry.get()
    connection.execute(
        "INSERT INTO registrations (name, email, mobile, college, course) VALUES (?, ?, ?, ?, ?)",
        (name, email, mobile, college, course)
    )

    connection.commit()

    print("Registration successful")
name_label = tk.Label(window, text = "Name")
name_label.pack()
name_Entry = tk.Entry(window)
name_Entry.pack()
email_label = tk.Label(window, text = "Email")
email_label.pack()
email_Entry = tk.Entry(window)
email_Entry.pack()
mobile_label = tk.Label(window, text = "Mobile Number")
mobile_label.pack()
mobile_Entry = tk.Entry(window)
mobile_Entry.pack()
college_label = tk.Label(window, text = "College Name")
college_label.pack()
college_Entry = tk.Entry(window)
college_Entry.pack()
course_label = tk.Label(window, text = "Course")
course_label.pack()
course_Entry = tk.Entry(window)
course_Entry.pack()
register_button = tk.Button(window, text = "Register", command=register)
register_button.pack()
window.mainloop()
