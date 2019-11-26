import sqlite3

def create_student(first_name, last_name, home_room):
    with sqlite3.connect('Ferrall.db') as connection:
        cursor = connection.cursor()
        sql_data = {"first_name": first_name,
                    "last_name": last_name,
                    "home_room": home_room}
        INSERT_SQL = """INSERT INTO students(first_name, last_name, home_room)
                    VALUES (:first_name, :last_name, :home_room);"""
        cursor.execute(INSERT_SQL, sql_data)
        return cursor.lastrowid

if __name__ == "__main__":
    print(create_student("John", "Schmitt", 10))