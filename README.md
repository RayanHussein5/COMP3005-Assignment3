Student Database Management System
COMP 3005 Assignment - A Python application for managing student records in PostgreSQL.
Video Demonstration
[Insert your video link here]

Prerequisites

Python 3.7+
PostgreSQL 12+
pgAdmin 4 (optional)


Installation
1. Install Python Library
bashpip install psycopg2-binary
2. Set Up Database

Open pgAdmin or psql
Run Database_setup.sql to create the table
Run Database_insert.sql to add initial data

3. Configure Connection
Edit test.py and update your database credentials:
pythonconn = psycopg2.connect(
    host="localhost",
    database="DataBase",
    user="postgres",
    password="YOUR_PASSWORD",  # Change this
    port=5432                   # Default is 5432, not 5433
)

Running the Application
bashpython test.py
To test different functions, uncomment the desired function calls in the if __name__ == "__main__": section.

Functions
check_connection()
Connects to the PostgreSQL database and checks for errors.
getAllStudents(conn)
Retrieves and displays all student records.
Example:
pythongetAllStudents(conn)
addStudent(first_name, last_name, email, enrollment_date, conn)
Adds a new student to the database with an auto-generated ID.
Example:
pythonaddStudent("John", "Doe", "john@example.com", "2025-09-01", conn)
updateStudentEmail(student_id, new_email, conn)
Updates the email address for a specific student.
Example:
pythonupdateStudentEmail(4, "newemail@example.com", conn)
deleteStudent(student_id, conn)
Deletes a student record by student ID.
Example:
pythondeleteStudent(4, conn)

Troubleshooting
Connection Error?

Check PostgreSQL is running
Verify your password and port number
Default port is 5432 (not 5433)

Module Not Found?
bashpip install psycopg2-binary
