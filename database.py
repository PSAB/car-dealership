import psycopg2
import credentials

def create_table():
    # Connect to database:
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    # Create a cursor object:
    cur = conn.cursor()
    # Queries go here:
    cur.execute("CREATE TABLE IF NOT EXISTS Cars(cid SERIAL PRIMARY KEY, make VARCHAR(20), model VARCHAR(20), year INTEGER)")
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

def insert(make, model, year):
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    cur = conn.cursor()
    cur.execute("INSERT INTO Cars(make, model, year) VALUES ('{}', '{}', {})".format(make, model, year))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
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
# print(view())