import sqlite3

def create_table():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, age, course):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name, age, course) VALUES (?, ?, ?)', (name, age, course))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    data = c.fetchall()
    conn.close()
    return data

def delete_student(name):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE name = ?', (name,))
    conn.commit()
    conn.close()
