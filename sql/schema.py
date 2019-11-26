import sqlite3

def schema(dbpath="application.db"):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROP_SQL = "DROP TABLE IF EXISTS students;"
        cur.execute(DROP_SQL)

        CREATE_SQL = """CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(128),
            last_name VARCHAR(128) NOT NULL,
            gpa FLOAT,
            bio TEXT,
            age INTEGER
        );"""
        cur.execute(CREATE_SQL)

if __name__ == "__main__":
    schema()