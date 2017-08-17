import sqlite3

with sqlite3.connect('sample.db') as connection:
    cur = connection.cursor()
    # cur.execute("""DROP TABLE posts IF EXISTS""")
    cur.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
    cur.execute('INSERT INTO posts VALUES("FLASK", "MICRO PYTHON FRAMEWORK")')
    cur.execute('INSERT INTO posts VALUES("PYTHON", "HIGH LEVEL PROGRAMMING LANGUAGE")')
    cur.execute('INSERT INTO posts VALUES("DJANGO", "BATTERY PYTHON FRAMEWORK")')