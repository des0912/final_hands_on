import sqlite3

# Connect to the database (creates a new one if not exists)
conn = sqlite3.connect("university.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INTEGER PRIMARY KEY,
        StudentName TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        CourseID INTEGER PRIMARY KEY,
        CourseName TEXT,
        StudentID INTEGER,
        ProfessorID INTEGER,
        FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
        FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Professors (
        ProfessorID INTEGER PRIMARY KEY,
        ProfessorName TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS CoursesProfessors (
        CourseID INTEGER,
        ProfessorID INTEGER,
        FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
        FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Assignments (
        AssignmentID INTEGER PRIMARY KEY,
        AssignmentName TEXT,
        StudentID INTEGER,
        FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
