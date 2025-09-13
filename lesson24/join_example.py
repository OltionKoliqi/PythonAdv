import sqlite3

from fastapi.perseritje import Student
from lesson24.main import cursor

conn = sqlite3.connect(example.db)

cursor.execute('''
    CREATE TABLE IF NOT EXIST students (
        student_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXIST courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        student_id INTEGER,
        FOREIGN KEY(student_id) REFERENCE students(student_id)
        
    )
''')

cursor.execute("INSERT INTO students (name) VALUES ('Alice')")
cursor.execute("INSERT INTO students (name) VALUES ('Bob')")

cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('Math', 1) ")
cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('Science', 2) ")
cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('Art', 3) ")


conn.commit()

cursor.execute('''
    SELECT students.name, courses.course_name from students
    JOIN courses on students.student_id = courses.student_id
''')

rows = cursor.fetchall()

for row in rows:
    print(f"Student: {row[1]}, Course: {row[1]}")

conn.close


































