import sqlite3

def create_table():
    # Connect to database:
    conn = sqlite3.connect("lite.db")
    # Create a cursor object:
    cur = conn.cursor()
    # Queries go here:
    cur.execute("CREATE TABLE IF NOT EXISTS Cars(cid INTEGER PRIMARY KEY AUTO_INCREMENT, make VARCHAR(20), model VARCHAR(20)), year INTEGER")
    cur.execute("INSERT INTO cars VALUES ('Toyota', 'Corolla', 2019), ('Toyota', '4Runner', 2020), ('Toyota', 'Land Cruiser', 2020)")
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()