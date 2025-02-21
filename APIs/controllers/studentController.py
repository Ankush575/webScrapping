# controller file in which all the business logic is written for CRUDoperations
from db import connectTodatabase


def execute_query(sql, params=None, multiple=False, fetch=False):
    """Executes a single or multiple SQL queries, optionally fetching results."""
    conn = connectTodatabase()
    if conn:
        try:
            # Fetch results as dictionaries
            cursor = conn.cursor(dictionary=True)
            if multiple:
                cursor.executemany(sql, params)
            elif params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            if fetch:
                result = cursor.fetchall()  # Fetch query results
                cursor.close()
                conn.close()
                return result

            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f" Database error: {e}")
            return False
    else:
        return False


# function to insert a single student


def insertSingleStudent(id, firstName, lastName, rollNumber, email, age):
    sql = """
        INSERT INTO students (id, firstName, lastName, rollNumber, email, age)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    params = (id, firstName, lastName, rollNumber, email, age)
    if execute_query(sql, params):
        return {"success": True, "message": "Student inserted successfully!"}
    else:
        return {"success": False, "message": "Error inserting student."}


# function to insert multiple students
def insertMultipleStudents(students):
    sql = """
    INSERT INTO students(id, firstName, lastName, rollNumber, email, age)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    params = [(s["id"], s["firstName"], s["lastName"],
               s["rollNumber"], s["email"], s["age"]) for s in students]

    if execute_query(sql, params, multiple=True):
        return {"success": True, "message": "Students inserted successfully!"}
    else:
        return {"success": False, "message": "Error inserting students."}


# function to fetch all the students from database
def fetchAllStudentsFromDatabase():
    sql = "SELECT * FROM students;"
    students = execute_query(sql, fetch=True)
    if students is not False:
        return {"success": True, "data": students}
    else:
        return {"success": False, "data": "No students found."}
