# model file in which the schema of the table is defined
from db import connectTodatabase


def creationOfTable():
    conn = connectTodatabase()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS students(
                                            id INT PRIMARY KEY,
                                            firstName varchar(30),
                                            lastName VARCHAR(30),
                                            rollNumber INT(10),
                                            email VARCHAR(30) UNIQUE,
                                            age INT(20) NOT NULL
                                            );
                                            """)
        conn.commit()
        cursor.close()
        conn.close()

        print("Students table created succssfully.....!")
    else:
        print("Error creating the table..")


creationOfTable()
