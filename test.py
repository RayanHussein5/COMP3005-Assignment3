import psycopg2


#this function will connect us to the server
#It will as well check if there was a connection error
def check_connection():
    
    try: 
        conn = psycopg2.connect(
        host="localhost",
        database="DataBase",
        user="postgres",
        password="Itstimetoreacte5@",
        port=5433 )

        print("---Connected to Server!---")
        


        return conn
    
    except Exception as e: 
        print("---Connection Error---")
        print("Info about error: ", e)

        return None


 

#get all the student rows and display them
def getAllStudents(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students;")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

def addStudent(first_name, last_name, email, enrollment_date, conn):
    cursor = conn.cursor()
    
    # Get the current max student_id
    cursor.execute("SELECT COALESCE(MAX(student_id), 0) FROM students;")
    max_id = cursor.fetchone()[0]
    next_id = max_id + 1  # increment by 1
    
    # Insert the new student with this next_id
    cursor.execute(
        """
        INSERT INTO students (student_id, first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s, %s);
        """,
        (next_id, first_name, last_name, email, enrollment_date)
    )
    
    conn.commit()
    print(f"Student added successfully with ID {next_id}!")
    return next_id



def updateStudentEmail(student_id, new_email, conn):
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE students
           SET email = %s
           WHERE student_id = %s;""",
        (new_email, student_id)
    )
    conn.commit()
    print(f"the email for row {student_id} was updated to {new_email}")
    

#this function will allow us to remove a student from the relation
def deleteStudent(student_id, conn):
    cursor = conn.cursor()
    cursor.execute(
        """DELETE FROM students
           WHERE student_id = %s;""",
           (student_id,)
    )
    conn.commit()
    print(f"row {student_id} has been deleted succesfully")



if __name__ == "__main__":

    conn = check_connection()


    #getAllStudents(conn)

    #addStudent("Asaad", "Husein", "asaadhusein@gmail.com", "2025-09-01", conn)

    deleteStudent(4, conn)

    #updateStudentEmail(4, "gameboy@gmail.com", conn)
    print("\n")
    #getAllStudents(conn)










