import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary real
)'''
)


cursor.execute('''
    INSERT INTO employees (name, position, department, salary)
     values (?,?,?,?)
     ''', ('John', 'Software Engineer','IT', 70000.00)
)

connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall()

for row in rows:
    print(rows)

cursor.execute('''
    UPDATE employees SET salary = ?
    WHERE name = ?
''', (80000.00, 'John')
)

connection.commit()

cursor.execute('''
    DELETE FROM employees WHERE id = ?
''', (1,))

connection.commit()
cursor.close()
connection.close()






























