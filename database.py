import psycopg2
import credentials

def create_table():
    # Connect to database:
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    # Create a cursor object:
    cur = conn.cursor()
    # Queries go here:
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(essn INTEGER PRIMARY KEY, name VARCHAR(40) NOT NULL, salary FLOAT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS Buyer(bssn INTEGER PRIMARY KEY, name VARCHAR(40) NOT NULL, insurance VARCHAR(30) NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS Cars(cid SERIAL PRIMARY KEY, make VARCHAR(20) NOT NULL, model VARCHAR(20) NOT NULL, year INTEGER NOT NULL, category VARCHAR(20) NOT NULL, fuel_type VARCHAR(20) NOT NULL, list_price FLOAT, miles INTEGER, commission FLOAT, purchase_date DATE, payment_type VARCHAR(20), price FLOAT, payment FLOAT, bssn INTEGER, essn INTEGER, FOREIGN KEY (bssn) REFERENCES Buyer(bssn), FOREIGN KEY (essn) REFERENCES Employee (essn))")
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

def delete(value, condition):
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    cur = conn.cursor()
    cur.execute("DELETE FROM Cars WHERE {} = '{}'".format(value, condition))
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

def sample():
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    cur = conn.cursor()
    cur.execute("DROP TABLE Cars")
    # rows = cur.fetchall()
    conn.commit()
    conn.close()
    # return rows


# sample()
create_table()

# insert('Toyota', 'Camry', 2019)
# insert('Toyota', '4Runner', 2019)
# insert('Toyota', 'Camry', 2019)
# insert('Toyota', 'Camry', 2019)

# delete('model', '4Runner')
# print(view())