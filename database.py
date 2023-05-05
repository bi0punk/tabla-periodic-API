import sqlite3

conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS my_table 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, value INTEGER)''')

# insert data
c.execute("INSERT INTO my_table (name, value) VALUES ('Item 1', 100)")
c.execute("INSERT INTO my_table (name, value) VALUES ('Item 2', 200)")

# commit changes
conn.commit()

# retrieve data
c.execute('SELECT * FROM Elements;')
rows = c.fetchall()
for row in rows:
    print(row)

# close connection

conn.close()