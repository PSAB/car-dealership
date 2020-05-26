import psycopg2

def create_table():
    # Connect to database:
    conn = sqlite3.connect("lite.db")
    # Create a cursor object:
    cur = conn.cursor()
    # Queries go here:
    cur.execute("CREATE TABLE IF NOT EXISTS Cars(cid INTEGER PRIMARY KEY AUTOINCREMENT, make TEXT, model TEXT, year INTEGER)")
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

def insert(make, model, year):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Cars(make, model, year) VALUES ('{}', '{}', {})".format(make, model, year))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cars")
    # fetch the query results:
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

create_table()
insert('Toyota', 'Camry', 2019)
insert('Toyota', '4Runner', 2019)
insert('Toyota', 'Camry', 2019)
insert('Toyota', 'Camry', 2019)
print(view())