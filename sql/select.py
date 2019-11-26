import sqlite3

with sqlite3.connect('Ferrall.db') as connection: # REQUIRED
    connection.row_factory = sqlite3.Row # this line gives you rows as dictionary like objects
    cursor = connection.cursor() # REQUIRED
    cursor.execute("SELECT * FROM william;") # for select you execute and then fetch
    rows = cursor.fetchall()
    for row in rows:
        pass
        #print(dict(row))
    

def get_movie(id):
    with sqlite3.connect('Ferral.db') as connection:
        cursor.execute("SELECT * FROM william WHERE id=?", (id,)) # (x,) is a single element tuple
        return tuple(cursor.fetchone())

def get_by_info(movie, year):
    with sqlite3.connect('Ferral.db') as connection:
        query_data = {"movie": movie, "year": year}
        cursor.execute("SELECT * FROM william WHERE movie=:movie AND year=:year", query_data) # (x,) is a single element tuple
        return tuple(cursor.fetchone())

if __name__ == "__main__":
    print(get_movie(8))