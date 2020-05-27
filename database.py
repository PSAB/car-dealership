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

def insert_car(make, model, year, fuel_type, list_price, miles, category):
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Cars(make, model, year, fuel_type, list_price, miles, category) VALUES ('{make}', '{model}', {year}, '{fuel_type}', {list_price}, {miles}, '{category}')")
    conn.commit()
    conn.close()

def edit_car(value, new_condition, cid):
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    cur = conn.cursor()
    cur.execute(f"UPDATE Cars SET {value} = {new_condition} WHERE cid = '{cid}'")
    conn.commit()
    conn.close()

def delete_car(cid):
    conn = psycopg2.connect(f"dbname={credentials.dbname} user={credentials.user} password={credentials.password} host={credentials.host} port={credentials.port}")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM Cars WHERE cid = '{cid}'")
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
# create_table()
# insert_car('Toyota', 'Supra', 2020, 'Gas', 49995, 7, 'Sport')
# insert_car('Toyota', '4Runner', 2018, 'Gas', 42995, 13266, 'Sport')
# edit_car('list_price', 40599, 2)
# delete_car(3)

# delete('model', '4Runner')
# print(view())